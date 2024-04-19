import random
from random import *

#0.000000-9.9999999 소수점의 결과값 리턴
print(random.random())

#10-20사이의 랜덤 소수점의 결과값을 리턴
print(random.uniform(10,20))

#1부터 3미만까지 랜덤숫자
print(random.randrange(1,3))


#리스트 내에 랜덤 1개
print(random.choice([1,2,3,4,5]))
print(random.choice([1,2,3,4,5]))


#리스트 내에 랜덤으로 k개를 선택, k가 리스트 개수보다 많으면 에러
print(random.sample([1,2,3,4,5],k=3))

#리스트의 요소를 랜덤으로 섞음
a_list=[1,2,3,4,5]
random.shuffle(a_list)# 출력을 하는 것이 아니라,a_list 결과를 저장시켜줌
print(a_list)


#1부터 10 이하,범위 내 랜덤 int를 1개 선택
print(random.randint(1,10))

# import math
# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))


