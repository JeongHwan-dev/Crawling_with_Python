# 음식점 href 크롤링

from bs4 import BeautifulSoup
import requests
import json

custom_header = {
    'referer': 'https://www.mangoplate.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


def get_restaurants(name):
    # 검색어 name 이 들어왔을 때 검색 결과로 나타나는 식당들
    restaurant_list = []

    url = "https://www.mangoplate.com/search/" + name
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    restaurants = soup.find_all("div", class_="list-restaurant-item")

    for rest in restaurants:
        info = rest.find("div", class_="info")
        href = "https://www.mangoplate.com/" + info.find("a")["href"]
        title = info.find("h2").get_text().replace('\n', '').replace(' ', '')
        restaurant_list.append([title, href])

    return restaurant_list


def main():
    name = input("검색어를 입력하세요.: ")

    restaurant_list = get_restaurants(name)

    print(restaurant_list)


if __name__ == "__main__" :
    main()
