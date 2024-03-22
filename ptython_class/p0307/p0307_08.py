import random

#random.random()

#0-1사이의 랜덤실수 생성  0.00000~0.999999
print(random.random())

#0,3까지 정수형 랜덤숫자 생성
print(random.randint(0,3))

#0,2까지 랜덤숫자를 생성
print(random.randrange(0,3))

# 리스트를 랜덤으로 섞기
list=[1,2,3,4,5,6,7]
print(list)
random.shuffle(list)
print(list)

#리스트에서 1개를 랜덤으로 추출
print(random.choice(list))

#리스트에서 해당되는 개수만큼 랜덤으로 추출(중복이 안되는 상태에서)
print(random.sample(list,4))

w_list=["토마토","바나나","사과","배","메론","복숭아"]

print(random.sample(w_list,3)) #무작위로 3개 골라서 샘플(중복이 안되는 상태에서)

fruit={'peach':'복숭아','orange':'오렌지',
       'apple':'사과','pear':'배','grapes':'포도',
       'mango':'망고','kiwi':'키위'}