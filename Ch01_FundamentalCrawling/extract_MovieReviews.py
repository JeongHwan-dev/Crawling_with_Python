# 영화 후기 수집하기

import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환
    result = []

    ul = soup.find("ul", class_="rvw_list_area")

    for li in ul.find_all("li"):
        result.append(li.find("strong").get_text())

    return result


def main():
    custom_header = {
        'referer': 'https://movie.naver.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36'
    }
    url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=168058#"
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력
    print(crawling(soup))


if __name__ == "__main__":
    main()
