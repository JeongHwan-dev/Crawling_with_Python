# 음식점 리뷰 크롤링

import requests
import json

custom_header = {
    'referer': 'https://www.mangoplate.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}


def get_reviews(code):
    comments = []
    i = 0

    while True:
        url = f"https://stage.mangoplate.com/api/v5/restaurants/DJjW5pG4aw/reviews.json?language=kor&device_uuid=IlDr216107044974864449Bona&device_type=web&start_index={i}&request_count=5&sort_by=2"

        req = requests.get(url, headers=custom_header)

        if req.status_code == requests.codes.ok:
            print("접속 성공")
            reviews = json.loads(req.text)

            if len(reviews) == 0:
                break
            for review in reviews:
                comment = review["comment"]
                text = comment["comment"]
                comments.append(text.replace('\n', ''))

        else:
            print("Error code")

        i += 50

    return comments


def main():
    href = "/restaurants/DJjW5pG4aw"
    print(get_reviews(href))


if __name__ == "__main__":
    main()

