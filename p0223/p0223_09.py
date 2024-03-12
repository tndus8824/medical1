import datetime

now=datetime.datetime.now() # 현재를 가져옴
print(now)#2024-02-23 13:03:26.739389
month=now.month # 현재 월

# 현재가 봄 여름 가을 겨울
# 12,1,2, 겨울. 3,4,5 봄  6,7,8 여름  9,10,11 가을

if  month ==3 or month ==4 or month ==5 : #3,4,5
    print("봄입니다")
elif month ==6 or month ==7 or month ==8 : #6,7,8
    print("여름입니다")
elif month ==9 or month ==10 or month ==11: #9,10,11
    print("가을입니다")
else:
    print("겨울입니다") #12,1,2,
    
print("지금은 {}월 입니다".format(month))