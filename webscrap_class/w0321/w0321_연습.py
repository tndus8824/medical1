import requests
from bs4 import BeautifulSoup
url=""
headers={}
res=requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

print(soup.title.text)
print(soup.title.a)#soup a태그 사용
print(soup.title.a.attrs)#soup a 태그의 속성값출력
print(soup.title.a["href"])#soup a 태그 선택속성값출력