# 주식 데이터 크롤링

import requests
import re
from bs4 import BeautifulSoup


# 기업에 대한 정보를 크롤링하는 함수입니다.
def crawling(soup):
    stock = []
    data = []

    name_list = []
    price_list = []

    # stock_index = soup.find("tbody")
    #
    # for index in stock_index.find_all("tr"):
    #     stock.append(index.get_text())

    tbody = soup.find("tbody")

    # for tr in tbody.find_all("tr"):
    #     for div in tr.find_all("div", class_="name_area"):
    #          name = div.get_text().replace('*', '')
    #         print(name)

    for tr in tbody.find_all("tr"""):
        name = tr.find("div", class_="name_area").get_text()
        price = tr.find("span", class_="tah p11 red02").get_text().replace(' ', '').replace('\t', '')
        print(price)
        print(name)


    # for div in tbody.find_all("div", class_="name_area"):
    #     name = div.get_text().replace("*", '')
    #     name_list.append(name)
    #
    # for td in tbody.find_all('td', class_="number"):
    #     price = td.get_text().replace('\n', '').replace('\t', '')
    #     # name = tr.get_text().replace('\n', '').replace('\t', '')
    #     print(price)
    #     stock.append(price)
    # return stock


def main():
    # 주어진 url을 크롤링하세요.
    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36'
    }
    url = "https://finance.naver.com/sise/sise_group_detail.nhn?type=upjong&no=235"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    # 현재가가 오름차순이 되도록 data 딕셔너리를 출력하세요.
    s = crawling(soup)
    print(s)


if __name__ == "__main__":
    main()
