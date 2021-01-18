# SBS 뉴스 최신 기사 목록의 내용 수집하기

import requests
from bs4 import BeautifulSoup


def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환
    # 각각의 href 페이지에 들어있는 기사 내용을 반환
    div = soup.find("div", class_="text_area")
    result = div.get_text().replace('\n', '').replace('\xa0', '')

    return result


def get_href(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환
    # 상위 페이지에서의 href를 찾아 리스트로 반환
    result = []

    div = soup.find("div", class_="w_news_list type_issue")

    for a in div.find_all("a", class_="news"):
        result.append("https://news.sbs.co.kr/" + a["href"])

    return result


def main():
    list_href = []
    list_content = []

    url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)
    print(list_href)

    for url in list_href:
        href_req = requests.get(url)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result = crawling(href_soup)
        list_content.append(result)

    print(list_content)


if __name__ == "__main__":
    main()