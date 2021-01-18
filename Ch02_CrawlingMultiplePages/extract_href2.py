# 네이트 최신뉴스 href 수집하기

import requests
from bs4 import BeautifulSoup


def get_href(soup):
    # 각 기사에 접근할 수 있는 href 를 리스트로 반환
    result = []

    div_list = soup.find_all("div", class_="mduSubjectList")

    for div in div_list:
        result.append("https:" + div.find("a")["href"])

    return result


def main():
    list_href = []

    # href 수집할 사이트 주소 입력
    url = "https://news.nate.com/recent?mid=n0100"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)

    print(list_href)


if __name__ == "__main__":
    main()
