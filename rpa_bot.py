# rpa_bot.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def submit_to_external_portal(data, headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        # Example URL — replace with real hospital portal
        driver.get("https://example-hospital-portal/book")
        time.sleep(1)
        # The element selectors below are placeholders — inspect the real site and replace IDs/names.
        driver.find_element(By.NAME, "patient_name").send_keys(data["Name"])
        driver.find_element(By.NAME, "patient_email").send_keys(data["Email"])
        driver.find_element(By.NAME, "patient_phone").send_keys(data["Phone"])
        driver.find_element(By.NAME, "date").send_keys(data["AssignedDate"])
        driver.find_element(By.NAME, "time").send_keys(data["AssignedTime"])
        driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        time.sleep(2)
        # optionally fetch confirmation text
        return True
    except Exception as e:
        print("RPA submission failed:", e)
        return False
    finally:
        driver.quit()
