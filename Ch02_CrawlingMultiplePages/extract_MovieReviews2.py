# 특정 영화 리뷰 추출하기
import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환
    # 1장 실습의 영화 리뷰 추출 방식과 동일
    result = []

    ul = soup.find("ul", class_="rvw_list_area")

    for li in ul.find_all("li"):
        result.append(li.find("strong").get_text())

    return result


def get_href(soup):
    ul = soup.find("ul", class_="search_list_1")

    a = ul.find("a")
    href = a["href"].replace('basic', 'review')

    return 'https://movie.naver.com' + href


def get_url(movie):
    return f'https://movie.naver.com/movie/search/result.nhn?query={movie}=all&ie=utf8'


def main():
    list_href = []

    custom_headeer = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36'
    }

    # 세션을 입력하세요.
    movie = input("영화 제목을 입력하세요. \n > ")

    url = get_url(movie)
    req = requests.get(url, headers=custom_headeer)
    soup = BeautifulSoup(req.text, "html.parser")

    movie_url = get_href(soup)

    href_req = requests.get(movie_url)
    href_soup = BeautifulSoup(href_req.text, "html.parser")

    list_href = crawling(href_soup)
    print(list_href)


if __name__ == "__main__":
    main()
