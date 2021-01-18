# 연합뉴스 속보 기사 제목 추출하기

import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환
    result = []

    div = soup.find("div", class_="list_body newsflash_body")

    for a in div.find_all("a"):
        result.append(a.get_text())

    return result


def main():
   custom_header = {
       'referer': 'https://www.naver.com/',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/87.0.4280.141 Safari/537.36'
   }
   url = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"
   req = requests.get(url, headers=custom_header)
   soup = BeautifulSoup(req.text, "html.parser")

   # crawling 함수의 결과를 출력
   print(crawling(soup))


if __name__ == '__main__':
    main()


