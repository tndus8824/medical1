import requests
from bs4 import BeautifulSoup

url="https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")
movie_list=soup.find("ol",{"class":"movie_list"})



m_list=movie_list.find_all("li")
for i,m in enumerate(m_list):
    if i ==5:break
    print(f"[번호{i+1}]")
    print("-"*50)
    print(m.find("img")['data-original-src'])
    img_screen=m.find("img")['data-original-src']
    print(img_screen)
    # print(m.img['data-original-src'])
    #파일열기
    with open(f"movie_{i}.jpg","wb") as f:
        re_img=requests.get(img_screen)
        f.write(re_img.content) #파일 이름의 내용을 저장
#파일쓰기


print("개수: ", len(m_list))

