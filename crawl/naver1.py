# 네이버 오픈api 뉴스 검색
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError

url = "https://openapi.naver.com/v1/search/news.json"

headers = {
    "X-Naver-Client-Id": "EHklZTF7Z3z8fDw0pj7Y",
    "X-Naver-Client-Secret": "4mNVa6DNLC",
}

r = requests.get(url, headers=headers, params={"query": "파이썬"})

# soup 은 html 로 내려올 때만 / 지금은 json 으로 내려옴
# soup = BeautifulSoup(r.text, "lxml")

# json 가져오기
data = r.json()
# print(data)

# items 리스트
# print(data["items"])
for idx, item in enumerate(data["items"], 1):
    print(idx, item["title"], item["link"])
