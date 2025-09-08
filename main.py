from selenium_driver import create_chrome_driver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException


driver = create_chrome_driver(headless=True)

year, month, day = datetime.now().year, datetime.now().month, datetime.now().day

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
                print(f"{date}일은 휴일입니다.")
                continue
        except NoSuchElementException:
            pass

        try:
            if td.find_element(By.CSS_SELECTOR, "button.unselectable"):
                print(f"{date}일은 지난 날입니다.")
                continue
        except NoSuchElementException:
            pass

        try:
            if td.find_element(By.CSS_SELECTOR, "button.closed"):
                print(f"{date}일은 예약 마감됐습니다.")
                continue
        except NoSuchElementException:
            pass

        try:
            if td.find_element(By.CSS_SELECTOR, "button.today"):
                print(f"{date}일은 오늘입니다. 추후 로직 작성예정")
                continue
        except NoSuchElementException:
            pass

        try:
            if td.find_element(By.CSS_SELECTOR, "button.calendar_date"):
                print(f"{date}일은 예약 가능한 날입니다.")
        except NoSuchElementException:
            pass


if __name__ == "__main__":
    main()
