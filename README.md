# 🌌 NASA Exoplanet Catalog Scraper

This project is a web scraper built with Python, Selenium, and BeautifulSoup that extracts data from NASA's [Exoplanet Catalog](https://exoplanets.nasa.gov/exoplanet-catalog/). It collects key planetary information and exports it into a CSV file for further analysis.

## 🗂️ Project Structure

- `main.py` – Main scraper script  
- `data.csv` – Output CSV file with exoplanet data  
- `README.md` – Project documentation

---

## 🚀 Features

- Automates the browser using Selenium
- Parses the webpage with BeautifulSoup
- Extracts data on:
  - Planet name
  - Light years from Earth
  - Planet mass
  - Stellar magnitude
  - Discovery date
- Supports multi-page scraping
- Outputs results to `data.csv`

---

## 🧰 Technologies Used

- Python3
- Selenium
- BeautifulSoup4
- Chrome WebDriver
- CSV module

---

## 📄 Code Description

### `main.py`

This script performs the following tasks:

- **Imports Required Libraries**  
  Uses `selenium`, `BeautifulSoup`, `time`, and `csv` for browser automation, HTML parsing, delay handling, and data storage.

- **Initial Setup**  
  Launches Chrome browser using Selenium and opens the NASA Exoplanet Catalog URL.

- **Scraping Function (`scrape`)**  
  - Iterates through multiple catalog pages (up to 100 by default).
  - Parses the HTML content using BeautifulSoup.
  - Extracts planet names and relevant data like:
    - Light years from Earth
    - Planet mass
    - Stellar magnitude
    - Discovery date
  - Clicks the "Next" page button after scraping each page.

- **Data Storage**  
  Writes the collected data into a CSV file named `data.csv` with headers.

### Output

- A file named `data.csv` containing structured exoplanet data.
  
## 🛠️ Setup Instructions

### 1. Clone the Repository
  - git clone `https://github.com/Vevan05/Web-Scraping`
  - cd exoplanet-scraper

### 2. Install the Dependencies
  - `pip install selenium beautifulsoup4`

### 3. Download Chrome WebDriver
  - `https://chromedriver.chromium.org/downloads`
  - Add it to system PATH or project root.

### 4. Run the Script
  - `python main.py`
  - You will get the output in data.csv

---
