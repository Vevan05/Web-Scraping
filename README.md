# 🌌 NASA Exoplanet Catalog Scraper

This project is a web scraper built with Python, Selenium, and BeautifulSoup that extracts data from NASA's [Exoplanet Catalog](https://exoplanets.nasa.gov/exoplanet-catalog/). It collects key planetary information and exports it into a CSV file for further analysis.

## 🗂️ Project Structure

- `main.py` – Main scraper script  
- `exoplanets.csv` – Output CSV file with exoplanet data  
- `README.md` – Project documentation

## 🚀 Features

- Automates the browser using Selenium
- Parses the webpage with BeautifulSoup
- Extracts data on:
,Discovery Method,Planet Mass,Discovery Date,Orbital Radius,Orbital Period,Eccentricity
  - Planet name
  - Planet description
  - Planet radius
  - Planet type
  - Discovery method
  - Planet mass
  - Discovery date
  - Orbital radius
  - Orbital period
  - Eccentricity
- Supports multi-page scraping
- Outputs results to `exoplanets.csv`

## 🧰 Technologies Used

- Python3
- Selenium
- BeautifulSoup4
- Requests
- Chrome WebDriver
- Pandas module

## ⚙️ How It Works

### 1. Browser Initialization
- Launches a headless Chrome browser using Selenium
- Sets up WebDriver and explicit waits for dynamic content loading
- Uses the NASA Exoplanet Catalog URL with pagination support

### 2. Page Iteration
- Iterates through catalog pages (1 to 411)
- For each page:
  - Loads the page using Selenium
  - Waits until exoplanet items are visible
  - Extracts all exoplanet detail page links

### 3. Data Extraction
- For each exoplanet link:
  - Fetches the page using `requests` (faster than Selenium)
  - Parses HTML using BeautifulSoup
  - Extracts:
    - Title (from page heading)
    - Description
    - Key-value data from structured content blocks

### 4. Data Collection
- Stores extracted data as dictionaries in a list (`all_data`)
- Handles missing fields gracefully using try/except blocks

### 5. Periodic Saving & Restart
- Every 20 pages:
  - Saves current data to `exoplanets.csv`
  - Restarts the browser to prevent memory issues

### 6. Final Output
- After all pages are processed:
  - Converts collected data into a pandas DataFrame
  - Writes the final dataset to `exoplanets.csv`
- Closes the browser session

  
## 🛠️ Setup Instructions

### 1. Clone the Repository
  - git clone `https://github.com/Vevan05/Web-Scraping`
  - cd exoplanet-scraper

### 2. Install the Dependencies
  - `pip install selenium beautifulsoup4 pandas`

### 3. Download Chrome WebDriver
  - `https://chromedriver.chromium.org/downloads`
  - Add it to system PATH or project root.

### 4. Run the Script
  - `python main.py`
  - You will get the output in data.csv

---
