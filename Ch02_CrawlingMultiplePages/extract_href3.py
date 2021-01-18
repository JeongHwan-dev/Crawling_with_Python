# 다양한 섹션의 속보 기사 href 추출하기

import requests
from bs4 import BeautifulSoup


def get_href(soup):
    # 각 분야별 속보 기사에 접근할 수 있는 href 를 리스트로 반환
    result = []

    ul = soup.find("ul", class_="type06_headline")

    for a in ul.find_all("a", class_="nclicks(fls.list)"):
        result.append(a["href"])

    return result


def get_request(section):
    # 입력된 분야에 맞는 requests 객체를 반환
    # 아래 url에 쿼리를 적용한 것을 반환
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36'
    }

    url = "https://news.naver.com/main/list.nhn"
    sections = {
        "정치" : 100,
        "경제" : 101,
        "사회" : 102,
        "생활" : 103,
        "세계" : 104,
        "과학" : 105
    }

    req = requests.get(url, headers=custom_header, params={"sid1": sections[section]})

    return req


def main():
    list_href = []

    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n > ')
    req = get_request(section)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)
    print(list_href)


if __name__ == "__main__":
    main()
