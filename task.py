
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import bs4
import time
from datetime import datetime

driver_path = '/home/chioma/Documents/Sunday/web_scape/chromedriver'
options = webdriver.ChromeOptions()

# options.headless = True
driver = webdriver.Chrome(driver_path,options=options)
start_time = datetime.now()
print ('start_time',start_time)
driver = webdriver.Chrome(driver_path,options=options)
driver.maximize_window()
# url = 'https://www.youtube.com'
url = 'https://www.edmunds.com/cars-for-sale-by-owner/'
driver.get (url)

time.sleep(10)
# driver.get ('https://www.python.org/')

# path= '//input[@id="search"]'
zipcode_elements = driver.find_element_by_name('zip')
print ('zip >>', zipcode_elements)
# yield scrapy.Request(zipcode_element[0].get_attribute('href'))

zipcode_elements.clear()
zipcode_elements.clear()

# time.sleep(5)
zipcode_elements.send_keys(zipcode)
zipcode_elements.send_keys(Keys.RETURN)
print ('zzzz >>',zipcode_elements)

pages_links = driver.find_elements_by_css_selector('a.text-gray-darker') # for the pages links
print ('>>> pages',pages_links)
print ('last page',pages_links[-1].get_attribute("href"))
page_url,part_url, max_page_number =pages_links[-1].get_attribute("href").split('=')
page_base_url= page_url+part_url+'='
print ('base url: >>', page_base_url,'  max_page:', max_page_number)


links_elements = driver.find_elements_by_class_name('usurp-inventory-card-vdp-link') # for the cars links
# links_elements = driver.find_elements_by_class_name('slick-slider slick-carousel show-one fluid inventory-card-carousel slick-initialized') # for the cars links
for link in list(set(links_elements)):
    print ('link:', link.get_attribute("href"))
                
# print ('links:', links_elements)
print ('Total  pages  :', int(max_page_number))
print ('car objects per page :', len(list(set(links_elements))))
print (' Total car objects ', int(max_page_number)*len(list(set(links_elements))))
end_time = datetime.now()
print ('end_time',end_time)
