# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json, os

from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
from scrapy import signals
import pandas as pd


class CarsPipeline:

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('cars.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()


    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

        if os.path.exists('cars.csv'):
            #Convert CSV to xlsx using pandas 
            data_csv = pd.read_csv('cars.csv')

            #Rename the Headers 
            col_title = {'Vehicle_summary': 'Vehicle Summary','top_features_and_specs': 'Top Features & Specs'}
            data_csv.rename(columns=col_title,inplace=True)

            #Export to .xlsx file 
            data_csv.to_excel('cars.xlsx') 

            #Delete the .csv file 
            os.remove('cars.csv')
        
            

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item