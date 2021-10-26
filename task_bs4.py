
from time import sleep
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

driver_path = '/home/chioma/Documents/Sunday/web_scape/chromedriver'
options = webdriver.ChromeOptions()

# options.headless = True
# driver = webdriver.Chrome(driver_path,options=options)
start_time = datetime.now()
print ('start_time',start_time)
main_webpage=requests.get('https://www.edmunds.com/cars-for-sale-by-owner/')


main_soup=bs4.BeautifulSoup(main_webpage.content,'html.parser')

print (main_soup)

start_time = datetime.now()
print ('start_time',start_time)