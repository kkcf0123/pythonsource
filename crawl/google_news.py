# '파이썬' 뉴스 기사 크롤링 → 키워드만 바꿔 크롤링 하는 프로그램 구현
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def main(keword):
    url = "https://news.google.com/search?q=" + keword + "&hl=ko&gl=KR&ceid=KR%3Ako"

    try:
        with requests.Session() as s:
            r = s.get(url)
            soup = BeautifulSoup(r.text, "lxml")
            # print(soup)

            news_clipping = data_extract(soup)

            for news in news_clipping:
                for k, v in news.items():
                    print(f"{k} : {v}")
                print()

    except HTTPError as e:
        print(e.code)


def data_extract(soup):

    # article 찾기
    # yDmH0d > c-wiz:nth-child(29) > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(1) > c-wiz > article
    articles = soup.select("div.UW0SDc article")
    base_url = "https://news.google.com"

    news = []
    news_items = {}

    for article in articles:
        # print(article)

        # 제목 찾기
        # #yDmH0d > c-wiz > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(1) > c-wiz > article > div.m5k28 > div.B6pJDd > div > a
        link_title = article.select_one("div.B6pJDd a")
        # 제목 추출
        news_items["title"] = link_title.text

        # 뉴스기사 링크 추출
        # ./articles/CBMiMWh0dHBzOi8vd3d3Lm5ld3N3aXJlLmNvLmtyL25ld3NSZWFkLnBocD9ubz05ODU4OTPSAQA?hl=ko&gl=KR&ceid=KR%3Ako
        # base url + & . 제거
        news_items["href"] = base_url + link_title["href"][1:]

        # 작성자
        # <div class="a7P8l"><div class="vr1PYe" data-n-tid="9">e4ds 뉴스</div></div>
        news_items["writer"] = article.select_one("div.a7P8l div").text

        # 작성일자와 시간 2024-04-19T07:00:00Z
        # T 기준으로 분리
        # <time class="hvbAAd" datetime="2024-05-20T00:58:00Z">8일 전</time>
        report_date_time = article.select_one("time")

        if report_date_time:
            # split → ['2024-05-20', '00:58:00Z']
            report_date_time = report_date_time["datetime"].split("T")
            news_items["report_date"] = report_date_time[0]
            news_items["report_time"] = report_date_time[1]
        else:
            news_items["report_date"] = ""
            news_items["report_time"] = ""

        # print(title, href, writer, report_date, report_time)

        news.append(news_items)
        news_items = {}

    # 확인
    print(news[:3])
    return news


# [
#     {"title":"오픈소스 커뮤니티 노리는 공급망 공격, 국내 연구팀 기술로 차단한다",
#      "href":"",
#      "writer":"IT World",
#      "report_date":"",
#      "report_time":""}
# ]

if __name__ == "__main__":
    main("아이폰")
