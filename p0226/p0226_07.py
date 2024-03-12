#random 함수
from random import *

print(random())#0.0~1.0미만의 임의의 값 생성
print(int(random()*10)) #1.0~10.0 미만의 임의의 값 생성
print(int(random()*10)+1) #1.0~10.0 이하의 임의의 값 생성
print(int(random()*10)+1) #1.0~10.0 이하의 임의의 값 생성
#1 ~ 45 이하의 임의의 값 생성
print(int(random()*45)+1) #1.0~45.0 이하의 임의의 값 생성
print(randrange(1,46))#1.0~46.0 미만의 임의의 값 생성
print(randint(1,45))#1.0~45.0 이하의 임의의 값 생성

#해보세요 >>
#1~10사이의 숫자를 입력받아서
#랜덤한 숫자와 비교해 같은면 [당첨] 
# 다르면[랜덤숫자는 {}로 일치하지 않습니다.]

A=int(input("1~10사이의 숫자를 입력해주세요 >>> "))
B=randrange(1,11) #randint(1,10)

if A==B:
    print('[당첨]')
else:
    print('랜덤숫자는 {} 로 일치하지 않습니다.'.format(B))
    
    



