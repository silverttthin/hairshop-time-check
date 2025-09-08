from selenium_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from available_time_check import check_date
from calendar import monthrange


driver = create_chrome_driver(headless=True)

year, month, day = datetime.now().year, datetime.now().month, datetime.now().day
last_day = monthrange(year, month)[1]

# 빈자리는 0으로 채우기, 2자리 길이 + Decimal = :02d
url = (
    f"https://booking.naver.com/booking/13/bizes/920424/items/5109739?"
    f"area=ple&lang=ko&startDate={year}-{month:02d}-{day:02d}&theme=place"
)


def main():
    driver.get(url)

    # 선택자 부모 지정 이후 선택자표기 없이 태그 지정
    tds = driver.find_elements(By.CSS_SELECTOR, ".calendar_body td")

    for td in tds:
        date = td.find_element(By.CSS_SELECTOR, "span.num").text
        try:
            if td.find_element(By.CSS_SELECTOR, "button.unselectable.dayoff"):
                continue
        except NoSuchElementException:
            pass

        try:
            if td.find_element(By.CSS_SELECTOR, "button.unselectable"):
                continue
        except NoSuchElementException:
            pass

        try:
            if td.find_element(By.CSS_SELECTOR, "button.closed"):
                continue
        except NoSuchElementException:
            pass

        try:
            if btn := td.find_element(By.CSS_SELECTOR, "button.today"):
                available_time_list = check_date(btn, driver, date)
                print(f"{date}일 예약 가능한 시간 : {available_time_list}")
                continue
        except NoSuchElementException:
            pass

        try:
            if btn := td.find_element(By.CSS_SELECTOR, "button.calendar_date"):
                available_time_list = check_date(btn, driver, date)
                print(f"{date}일 예약 가능한 시간 : {available_time_list}")
                continue
        except NoSuchElementException:
            pass


if __name__ == "__main__":
    main()
