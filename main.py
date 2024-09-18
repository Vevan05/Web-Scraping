from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(2)

planets_data = []

def scrape():

    for i in range(100):
        print(f'Scrapping page {i+1} ...')

        soup = BeautifulSoup(browser.page_source, "html.parser")

        names = []
        info = []

        for ul_tag in soup.find_all(class_ = "hds-content-item"):
            infos = []
            for h in ul_tag.find_all("h3"):
                for i in h:
                    names.append(i)
            
            for j in ul_tag.find_all("span"):
                for k in j:
                    infos.append(k)

            for l in range(1, len(infos), 8):
                L = [infos[l], infos[l + 2], infos[l + 4], infos[l + 6]]
                info.append(L)

        for i in range(len(names)):
            x = []
            x.append(names[i])
            x.extend(info[i])
            planets_data.append(x)
        

        button = browser.find_element(By.CLASS_NAME, "page-numbers")
        browser.implicitly_wait(10)
        ActionChains(browser).move_to_element(button).click(button).perform()

    print("Data Scraped Completed!")

# Calling Method
scrape()

# Define Header
headers = ["name", "light_years_from_earth",
           "planet_mass", "stellar_magnitude", "discovery_date"]

with open("data.csv", "w+") as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(planets_data)