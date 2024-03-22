import requests
#웹에 접근해서 html 소스를 가져옴.

# res =requests.get("https://www.google.com/")
# res =requests.get("https://www.daum.net/")
res =requests.get("https://www.melon.com/")#접근막힘#<Response [406]>

print(res) #<Response [200]>=정상, [403],[404]=페이지없음,[500]=프로그램에러
print("코드 :  ",res.status_code)#리턴한 소스의 값을 출력
print(type(res.status_code))
if res.status_code ==requests.codes.ok:#requests.codes.ok:200
    print("정상페이지 호출입니다.")
else:
    print("에러코드발생")
#requests를 통해 html소스를 출력
print(res.text)
print("-"*40)
res.raise_for_status()#200 코드가 200이 아니면 오류처리 해서 자동멈춤
#<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head