import scrapy
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from cars.items import CarsItem


class CarsSpider(scrapy.Spider):
    name = 'cars'

   
    def start_requests(self):
        zipcode = input('Kindly insert the zipcode you will like to search with : ')
        settings = get_project_settings()  # This is to call my settings I declared in the settings.py
        driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
       
        driver = webdriver.Chrome(driver_path,options=options)

        driver.maximize_window() #This is to make the browser run on fullscreen due to some flex property on the websites

        url = 'https://www.edmunds.com/cars-for-sale-by-owner/'
        
        #This is to load the url
        driver.get (url)
     

        zipcode_elements = driver.find_element_by_name('zip')
        print ('zip >>', zipcode_elements)

        #This is to clear the text input  field before inserting the new zip code
        zipcode_elements.clear()
        zipcode_elements.clear()   
        
        zipcode_elements.send_keys(zipcode)
        zipcode_elements.send_keys(Keys.RETURN)

        pages_links = driver.find_elements_by_css_selector('a.text-gray-darker') # This is to get all the urls for the other pages
        page_url,part_url, max_page_number =pages_links[-1].get_attribute("href").split('=')
        page_base_url= page_url+part_url+'='
        pages = int(max_page_number)

        
        first_links_elements = driver.find_elements_by_class_name('usurp-inventory-card-vdp-link') # for the cars links
     

        '''
        Since I am looping through all the pages and the pages are larger (over 300 pages), 
        I override it with this 5 pages (Useable once uncommented)  
        '''
        # pages = 2  
        
        print('Total Pages: ', pages)
                

        for i in range(1, pages+1):
            if i == 1 :
                links_elements = first_links_elements
            else:
                next_page_url = page_base_url+ str(i)
                driver.get(next_page_url)
                links_elements = driver.find_elements_by_class_name('usurp-inventory-card-vdp-link')

            for link in links_elements:
                try:
                    yield scrapy.Request(link.get_attribute('href'))
                except:
                    continue

        driver.quit()

    def parse(self, response):
        
        car = CarsItem()
        car['Name'] = response.css('h1 ::text').getall()
        car['Price'] = response.xpath('//div[@class="heading-2 mb-0"]/span/text()').extract_first()
        car['VIN'] = response.xpath('/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/div[2]/div/span[1]/text()[2]').extract_first()
        car['Vehicle_summary'] =  [response.xpath('//div[@class="col"]/text()').extract()]
        car['top_features_and_specs'] = response.xpath('/html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[3]/div/div/section[5]/div/div[1]/div/text()').getall()
                
        
        yield car