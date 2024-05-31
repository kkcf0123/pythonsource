# 네이버 오픈api 책 검색

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = "도서검색"
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 100
ws.column_dimensions["D"].width = 20
ws.column_dimensions["E"].width = 20

ws.append(["번호", "isbn", "책제목", "저자", "할인가격"])

headers = {
    "X-Naver-Client-Id": "EHklZTF7Z3z8fDw0pj7Y",
    "X-Naver-Client-Secret": "4mNVa6DNLC",
}


start, num = 1, 1
for idx in range(3):
    # idx : 0~9
    start_num = start + (idx * 100)
    url = "https://openapi.naver.com/v1/search/book.json"
    params = {"query": "베르나르 베르베르", "display": "100", "start": str(start_num)}
    r = requests.get(url, headers=headers, params=params)

    # print(r.url)

    # json 가져오기
    data = r.json()
    # print(data)

    # items 리스트
    # print(data["items"])
    for idx, item in enumerate(data["items"], 1):
        ws.append([num, item["isbn"], item["title"], item["author"], item["discount"]])
        num += 1

base_dir = "./crawl/file/"
wb.save(base_dir + "naver_book.xlsx")
wb.close()
