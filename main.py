from selenium_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from datetime import datetime


driver = create_chrome_driver(headless=True)

start_date = datetime.now().strftime("%Y-%m-%d")

url = f"https://booking.naver.com/booking/13/bizes/920424/items/5109739?area=ple&lang=ko&startDate={start_date}&theme=place"

driver.get(url)

calendar_body = driver.find_element(By.CSS_SELECTOR, ".calendar_body")

