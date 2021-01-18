import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # 기사에서 내용츨 추출하고 반환
    div = soup.find("div", class_="_article_body_contents")

    result = div.get_text().replace('\n', '').replace('\t', '')

    return result


def get_href(soup):
    # 각 분야별 속보 기사에 접근할 수 있는 href를 리스트로 반환
    result = []

    for ul in soup.find_all("ul", class_="type06_headline"):
        for a in ul.find_all("a"):
            result.append(a["href"])

    return result


def get_request(section):
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

    req = requests.get(url, headers=custom_header, params={"sid1": sections[section]})\

    return req


def main():
    list_href = []
    result = []

    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36'
    }

    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')

    req = get_request(section)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)

    for href in list_href:
        href_req = requests.get(href, headers=custom_header)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))
    print(result)


if __name__ == "__main__":
    main()
