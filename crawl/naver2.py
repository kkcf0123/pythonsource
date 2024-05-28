# 네이버 오픈api 샵 검색
# 파싱은 차단되는 것도 있지만 오픈 api 는 서버에서 제공해 다 갖고 올 수 있음

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = "네이버 open"
ws.column_dimensions["B"].width = 100
ws.column_dimensions["C"].width = 60

ws.append(["순위", "상품명", "판매경로"])

url = "https://openapi.naver.com/v1/search/shop.json"

headers = {
    "X-Naver-Client-Id": "EHklZTF7Z3z8fDw0pj7Y",
    "X-Naver-Client-Secret": "4mNVa6DNLC",
}


start, num = 1, 0
for idx in range(10):
    # idx : 0~9
    start_num = start + (idx * 100)
    params = {"query": "아이폰", "display": "100", "start": str(start_num)}
    r = requests.get(url, headers=headers, params=params)

    print(r.url)

    # json 가져오기
    data = r.json()
    # print(data)

    # items 리스트
    # print(data["items"])
    for idx, item in enumerate(data["items"], 1):
        # print(idx, item["title"], item["link"])  # <b>아이폰</b> title 태그 제거
        ws.append([num, item["title"], item["link"]])
        num += 1

base_dir = "./crawl/file/"
wb.save(base_dir + "naver.xlsx")
wb.close()
