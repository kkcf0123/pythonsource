from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import pandas as pd


def main():
    browser = set_chrome_driver()

    url = "https://www.youtube.com/watch?v=DMuVeWeEtns"
    browser.get(url)

    time.sleep(2)

    # 스크롤 움직이기
    interval = 5

    # 현재 문서 높이를 가져와서 저장
    # 유투브는 문서 디자인 상 body → documentElement
    prev_height = browser.execute_script("return document.documentElement.scrollHeight")

    while True:
        browser.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight)"
        )

        time.sleep(interval)

        cur_height = browser.execute_script(
            "return document.documentElement.scrollHeight"
        )

        if cur_height == prev_height:
            break

        prev_height = cur_height

    time.sleep(3)

    # 전체 소스를 BeautifulSoup 담기
    soup = BeautifulSoup(browser.page_source, "lxml")

    # 댓글 사용자의 아이디 및 코멘트 가져오기
    ids = soup.select("#author-text > span")
    comments = soup.select("#content-text > span")

    ids_list = []
    comments_list = []

    # 확인
    for idx in range(len(ids)):
        # print(ids[idx].text.strip(), comments[idx].text.strip())

        # 공백 제거
        clean_id = ids[idx].text.strip()
        clean_id = clean_id.replace("\n", " ")
        clean_id = clean_id.replace("\t", " ")
        ids_list.append(clean_id)

        clean_comment = comments[idx].text.strip()
        clean_comment = clean_comment.replace("\n", " ")
        clean_comment = clean_comment.replace("\t", " ")
        comments_list.append(clean_comment)

    # 데이터 프레임 생성
    dict_data = {"Id": ids_list, "Comments": comments_list}
    df = pd.DataFrame(dict_data)

    df.to_csv("./crawl/file/youtube.csv", index=False, encoding="utf-8-sig")

    time.sleep(5)


# 크롬으로 띄우기 위해 자동으로 크롬을 조작하기 위한 드라이버 지정
def set_chrome_driver():
    options = ChromeOptions()
    # options.add_argument("--start-maximized")  # 창 최대화
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


main()
