# web_scrape_scrapy




* Scope: Web Scraping of https://www.edmunds.com/cars-for-sale-by-owner/ to extract Cars and their details
* Tools Used : Scrapy, Selenium, Pandas

## Developer : Ajayi Sunday (sunnexajayi@gmail.com)



Chrome driver version used : 94.0.4606.61
OS : linux 

# How to Access and Test the project

1. A virtual environment environment needs to be created ( For example : you can used virtualenv webscrap_env)

2. I have a requirements.txt file that contains on the pip packages used.

3. Install the pip packages into the virtual environment ( You can use : pip -r install requirements.txt)

4. Please ensure you have a chrome browser on your PC while testing 

5. Please ensure that the chrome driver version is the same has your chrome browser ( If it is not, update your the attached chrome driver with one corresponding to your chrome browser. You can get the driver via : https://chromedriver.chromium.org/downloads )

6.  Run the application using 'scrapy crawl cars' from your OS terminal  ( Note: please ensure you are in the car directory before running the command) 

7. The name of the expected .xlsx file which should be gotten after running the application is *cars.xlsx*

8. The car.xlsx file is the piped output and can be found : /cars/ directory    

('sample_cars.xlsx' is a sample output file)


** Please note that by default it will scrape the car details for all the pages which takes times but 
   can uncomment the page count I set in line 56 in the  car_scrape.py  file  
