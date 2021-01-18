# Daum 증권 페이지에서 주가 크롤링

import requests
import json

custom_header = {
    'referer': 'https://finance.daum.net/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36'
}


def get_data():
    result = []
    url = "https://finance.daum.net/api/search/ranks?limit=10"
    req = requests.get(url, headers=custom_header)

    if req.status_code == requests.codes.ok:
        print("접속 성공")

        # JSON 데이터의 원하는 부분만 불러와 result 에 저장
        stock_data = json.loads(req.text)

        for d in stock_data["data"]:
            result.append([d['rank'], d['name'], d['tradePrice']])

    else:
        print("접속 실패")

    return result


def main():
    data = get_data()

    for d in data:
        print(d)


if __name__ == "__main__":
    main()
