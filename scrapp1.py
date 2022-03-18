from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import json

import requests

PATH = "C:\POLBAN MATERI\SEMESTER 2\proyek pengembangan perangkat lunak desktop\Pertemuan 6\Web scrapping 2 (Selenium)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://companiesmarketcap.com/largest-companies-by-number-of-employees/")

from datetime import datetime
x = datetime.now()

ListCompany = []

i = 1

for  company in driver.find_elements_by_tag_name("tbody"):
    for a in company.find_elements_by_tag_name("tr"):
        for img in a.find_elements_by_class_name("company-logo"):
            ListCompany.append(
                {"Rank": a.text.split("\n")[0],
                 "Name": a.text.split("\n")[1],
                 "Employee": a.text.split("\n")[3].split(" ")[0],
                 "National": a.text.split("\n")[3].split(" ")[3],
                 "Image" : img.get_attribute("src"),
                 "waktu_scraping": x.strftime("%Y-%m-%d pukul %H:%M:%S")
                }
        )
   
     
hasil_scraping = open("hasilscraping.json", "w")
json.dump(ListCompany, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()