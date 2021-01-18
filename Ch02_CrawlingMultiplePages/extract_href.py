# 각 기사의 href 수집하기

import requests
from bs4 import BeautifulSoup


def get_href(soup):
    # soup 에 저장되어 있는 각 기사에 접근할 수 있는 href 들을 담고 있는 리스트를 반환
    result = []

    ul = soup.find("ul", class_="list_news")

    for span in ul.find_all("span", class_="tit"):
        result.append(span.find("a")["href"])

    return result


def main():
    list_href = []

    url = "https://sports.donga.com/ent?p=1&c=02"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)
    print(list_href)


if __name__ == "__main__":
    main()
