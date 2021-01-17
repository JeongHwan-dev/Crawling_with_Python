from bs4 import BeautifulSoup

# index.html 을 불러와서 BeautifulSoup 객체를 초기화해 soup에 저장
soup = BeautifulSoup(open("index.html"), "html.parser")

# 1. 불러온 html 문서를 출력
print(soup)

print("=" * 50)

# 2. soup 를 사용하여 <p> 태그 부분의 텍스트를 출력
print(soup.find("p"))
print(soup.find("p").get_text())

print("=" * 50)

# 3. class 가 "elice" 인 <div> 태그 부분의 텍스트를 출력
print(soup.find("div"))
print("-" * 50)
print(soup.find("div", class_="elice"))
print("-" * 50)
print(soup.find("div", class_="elice").get_text())

print("=" * 50)

# 4. id 가 "main" 인 <div> 태그 부분의 텍스트를 출력
print(soup.find("div"))
print('-' * 50)
print(soup.find("div", id="main"))
print('-' * 50)
print(soup.find("div", id="main").get_text())