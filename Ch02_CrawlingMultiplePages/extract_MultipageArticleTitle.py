# 여러 페이지의 기사 제목 수집하기

import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환
    result = []

    ul = soup.find("ul", class_="list_news")

    for span in ul.find_all("span", class_="tit"):
        result.append(span.get_text())

    return result


def main():
    url = "https://sports.donga.com/ent"
    answer = []

    for i in range(0, 5):
        req = requests.get(url, params={'p': i * 20 + 1})
        soup = BeautifulSoup(req.text, "html.parser")
        answer += crawling(soup)

    # crawling 함수의 결과를 출력
    print(answer)


if __name__ == "__main__":
    main()
