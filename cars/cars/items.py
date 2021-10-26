# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarsItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Price = scrapy.Field()
    VIN = scrapy.Field()
    Vehicle_summary = scrapy.Field()
    top_features_and_specs = scrapy.Field()
    
