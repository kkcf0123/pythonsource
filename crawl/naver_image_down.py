from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from urllib.request import urlretrieve


def main():
    browser = set_chrome_driver()

    browser.get("https://www.naver.com")

    element = browser.find_element(By.ID, "query")

    element.send_keys("아이스크림")
    element.send_keys(Keys.ENTER)

    time.sleep(2)

    browser.find_element(
        By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a'
    ).click()

    time.sleep(2)

    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script("return document.body.scrollHeight")
    interval = 3

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        time.sleep(interval)

        cur_height = browser.execute_script("return document.body.scrollHeight")

        if cur_height == prev_height:
            break

        prev_height = cur_height

    # 스크롤 처음으로 움직이기
    browser.execute_script("window.scrollTo(0,0)")

    time.sleep(3)

    # 작은 이미지를 찾아오기
    imgages = browser.find_elements(By.CSS_SELECTOR, ".thumb img")

    count = 1
    for img in imgages:
        try:
            img.click()
            time.sleep(2)

            # 큰 이미지
            # //*[@id="main_pack"]/section[1]/div/div/div[1]/div[2]/div[1]/img
            img_url = browser.find_element(
                By.CSS_SELECTOR, "div.viewer_image img"
            ).get_attribute("src")
            print(img_url)

            # urlretrieve("다운로드받을경로", "저장경로")
            urlretrieve(img_url, "./crawl/download/download" + str(count) + ".jpg")
            count += 1
        except:
            pass

    time.sleep(3)


# 크롬으로 띄우기 위해 자동으로 크롬을 조작하기 위한 드라이버 지정
def set_chrome_driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")  # 창 최대화
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


main()
