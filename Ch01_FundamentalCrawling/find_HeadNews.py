# 네이버 헤드 뉴스 찾기

import requests
from bs4 import BeautifulSoup


def crawling(soup):
    result = []     # 결과를 저장할 리스트 선언

    # class 가 "list_issue"인 <div> 태그안에 있는 <a>태그의 텍스트 출력
    div = soup.find("div", class_="list_issue")

    for a in div.find_all("a"):
        result.append(a.get_text())

    return result


def main():
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36'
    }

    url = "https://naver.com"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력
    print(crawling(soup))


if __name__ == "__main__":
    main()
