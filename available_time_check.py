from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def check_date(btn: WebElement, driver: webdriver.Chrome, date: str):
    available_time_list = []
    btn.click()

    # 선택자 요소 간 공백 = 후손 선택자 의미
    time_btn_list = driver.find_elements(By.CSS_SELECTOR, "li.time_item button")

    for time_btn in time_btn_list:
        reservation_time = time_btn.text

        time_btn_class = time_btn.get_attribute("class")
        if "unselectable" in time_btn_class:
            continue
        available_time_list.append(reservation_time)
    return available_time_list
