# 검색 결과 음식점 리뷰 크롤링

from bs4 import BeautifulSoup
import requests
import json

custom_header = {
    'referer' : 'https://www.mangoplate.com/',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


def get_reviews(code):
    comments = []

    url = f"https://stage.mangoplate.com/api/v5{code}/reviews.json?language=kor&device_uuid=V3QHS15862342340433605ldDed&device_type=web&start_index=0&request_count=5&sort_by=2"
    req = requests.get(url, headers=custom_header)

    if req.status_code == requests.codes.ok:
        print("접속 성공")
        reviews = json.loads(req.text)
        for review in reviews:
            comment = review["comment"]
            comments.append(comment["comment"].replace('\n', ''))
    else:
        print("Error code")

    return comments


def get_restaurants(name):
    restaurant_list = []

    url = "https://www.mangoplate.com/search/" + name
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    restaurants = soup.find_all("div", class_="list-restaurant-item")

    for rest in restaurants:
        info = rest.find("div", class_="info")
        href = info.find("a")["href"]
        title = info.find("h2").get_text().replace('\n', '').replace(' ', '')
        restaurant_list.append([title, href])

    return restaurant_list


def main():
    name = input("검색어를 입력하세요.: ")

    restaurant_list = get_restaurants(name)

    for r in restaurant_list:
        print(r[0])
        print(get_reviews(r[1]))
        print('=' * 30)
        print('\n' * 2)


if __name__ == "__main__":
    main()

