import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

# url 변수에 담긴 url의 html 문서를 불러와 출력
req = requests.get(url)

# 응답 결과 출력(200: 성공, 404: 실패)
print(req.status_code)

# 불러운 html 문서의 텍스트 출력
print(req.text)


