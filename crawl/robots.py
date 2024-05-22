# 크롤링 : 주기적으로 / 무작위로 데이터 수집
# pip install requests
# pip install bequtifulsoup4
# pip install selenium

import requests

# 사이트 접속 → get 방식으로 파일 요청
urls = ["https://www.naver.com/", "https://www.python.org/"]

file_name = "robots.txt"

for url in urls:
    robots = requests.get(url + file_name)
    print(robots.text)
