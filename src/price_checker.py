import logging
from bs4 import BeautifulSoup
from selenium import webdriver
from browser import setup_browser
from utils import extract_product_title, extract_price
from email_utils import send_email_alert

def get_page_soup(driver: webdriver.Chrome, url: str) -> BeautifulSoup:
    driver.get(url)
    return BeautifulSoup(driver.page_source, "html.parser")

def track_price(url: str, target_price: float) -> None:
    driver = setup_browser()
    try:
        logging.info("🔍 Checking price...")
        soup = get_page_soup(driver, url)
        title = extract_product_title(soup)
        price = extract_price(soup)

        logging.info(f"📦 {title}")
        logging.info(f"💵 Current Price: ${price}")

        if price < target_price:
            logging.info("🎯 Target price met. Sending email...")
            send_email_alert(title, url)
        else:
            logging.info("No alert — price is still above target.")
    except Exception as e:
        logging.error(f"[ERROR] {e}")
        with open("debug_amazon.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
            logging.info("Saved debug HTML to 'debug_amazon.html'")
    finally:
        driver.quit()
        logging.info("Browser closed.")
