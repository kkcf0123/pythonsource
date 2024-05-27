import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from xlsx_write import write_excel_template
from datetime import datetime

# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=0 - 1페이지
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=1 - 2페이지
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=2 - 3페이지


userAgent = UserAgent()

headers = {"user-agent": userAgent.chrome}

# 데이터 담을 리스트 생성
# lists = []
lists = list()

with requests.Session() as s:

    for page in range(5):
        url = "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
        url = url + str(page)
        r = s.get(url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")
        # print(soup)
        # 타이틀, 시간 행 출력
        # #div_content > div.list_content > div.list_item.symph_row
        rows = soup.select("div.list_content > div.list_item.symph_row")

        for row in rows:

            # #div_content > div.list_content > div:nth-child(2) > div.list_title > a > span.subject_fixed
            title = row.select_one("div.list_title > a > span.subject_fixed")

            # #div_content > div:nth-child(4) > div.list_time > span > span
            time = row.select_one("div.list_time > span > span")

            # 2024-04-27 07:22:02 → 2024-04-27
            print(title.text.strip(), time.text.strip()[:10])
            lists.append([title.text.strip(), time.text.strip()[:10]])

        print()

    # 파일 저장 : clien_240527.xlsx
    # 오늘 날짜
    today = datetime.now().strftime("%Y%m%d")

    # [title, time]
    # 시트명 : 팁과강좌
    write_excel_template(f"clien_{today}.xlsx", "팁과강좌", lists)
