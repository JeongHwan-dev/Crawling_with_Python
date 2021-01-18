# 네이버 실시간 검색어 크롤링

import requests
import json

custom_header = {
    'referer': 'https://www.naver.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36'
}


def get_keyword_ranking():
    result = []

    url = "https://apis.naver.com/mobile_main/srchrank/srchrank?frm=main&ag=10s&gr=0&ma=1&si=1&en=1&sp=1"
    req = requests.get(url, headers=custom_header)

    if req.status_code == requests.codes.ok:
        print("접속 성공")

        data = json.loads(req.text)
        data = data["data"]

        for d in data:
            if len(d["keyword_synonyms"]) == 0:
                result.append([d["keyword"], None])
            else:
                result.append([d['keyword'], d['keyword_synonyms']])

    else:
        print("Error code")

    return result


def main():
    result = get_keyword_ranking()
    i = 1

    for keyword, synonyms in result:
        if synonyms:
            print(f"{i}번째 검색어 : {keyword}, 연관검색어 : {synonyms}")
        else:
            print(f"{i}번째 검색어 : {keyword}")

        i += 1


if __name__ == "__main__":
    main()

