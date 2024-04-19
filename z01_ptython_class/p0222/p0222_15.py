import datetime #날짜 관련 기능을 가져옴
now = datetime.datetime.now() # 오늘 날짜 시분초 가져옴
year=now.year
print(year) #2024
m=now.month
h=now.hour #시간
# print(now) #2024-02-22 17:08:47.427600

# print(now.year) #연도
# print(now.month) #월
# print(now.day)  #일
# print(now.hour)  #일
# print(now.minute)  #분
# print(now.second)  #초
if h <12:
    print("지금 현재 {}시 오전입니다".format(h))
else:
    print("지금 현재 {}시 오후입니다".format(h))
#1.짝수달입니다. 홀수달입니다.
#월
#겨울입니다.겨울이 아닙니다.
m=now.month
print(type(m)) # type을 알아보는 방법: <class 'int'>
#월 겨울 3-11월이면 겨울이 아닙니다. 그외의 경우에는 겨울입니다
#겨울입니다. 겨울이 아닙니다
if m%2 == 0:
    print("짝수달입니다")
else :
    print("홀수달입니다")
    
if 3<= m <=11 :
    print("겨울이 아닙니다")
else :
    print("겨울입니다")