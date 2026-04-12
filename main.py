from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

base_url = "https://science.nasa.gov/exoplanets/exoplanet-catalog/?page={}"

all_data = []

def extract_data_from_html(html):
    soup = BeautifulSoup(html, "html.parser")

    try:
        title = soup.select_one("h1.page-heading-md").get_text(strip=True)
    except:
        title = ""

    try:
        description = soup.select_one(".custom-fields span").get_text(strip=True)
    except:
        description = ""

    data = {}

    blocks = soup.select(".smd-acf-grid-col")

    for block in blocks:
        try:
            key = block.select_one(".text-bold").get_text(strip=True).replace(":", "")
            val_tag = block.select_one("span") or block.select_one("li span")
            value = val_tag.get_text(strip=True)
            data[key] = value
        except:
            continue

    return {
        "title": title,
        "description": description,
        **data
    }

for page in range(1, 412):
    print(f"\n--- Page {page} ---")

    driver.get(base_url.format(page))

    wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "a.hds-content-item-thumbnail")
    ))

    items = driver.find_elements(By.CSS_SELECTOR, "a.hds-content-item-thumbnail")
    links = [item.get_attribute("href") for item in items]

    print(f"Found {len(links)} items")

    for link in links:
        try:
            html = requests.get(link, timeout=10).text
            data = extract_data_from_html(html)
            all_data.append(data)
            print("Scraped:", data["title"])
        except Exception as e:
            print("Error:", e)

        time.sleep(0.1)

    if page % 20 == 0:
        pd.DataFrame(all_data).to_csv("exoplanets.csv", index=False, encoding="utf-8")
        print("Progress saved... restarting browser")

        driver.quit()
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 10)

df = pd.DataFrame(all_data)
df.to_csv("exoplanets.csv", index=False, encoding="utf-8")

driver.quit()

print("Saved to exoplanets.csv")