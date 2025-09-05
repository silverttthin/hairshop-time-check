from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_chrome_driver(headless: bool = True, wait_time: int = 10) -> webdriver.Chrome:
    # 크롬 브라우저 옵션 설정
    options = Options()
    
    if headless:
        options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
    
    # 추가 안정성을 위한 옵션들
    options.add_argument("--no-sandbox")  # 샌드박스 모드 비활성화 (리눅스 환경에서 필요)
    options.add_argument("--disable-dev-shm-usage")  # /dev/shm 사용 비활성화
    
    # 드라이버 인스턴스 생성
    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(wait_time)
    
    return driver
