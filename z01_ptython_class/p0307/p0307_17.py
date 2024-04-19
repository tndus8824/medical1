
import random
#크기가 10인 리스트 생성하는데, 7개는 0으로 3개는 1로 채우시오.

#[1,1,1,0,0,0,0,0,0,0]

num=[]
for i in range(10):
    num.append(0)
print(num)
num[0]=1
num[1]=1
num[2]=1
print(num)

list=[0]*10
for i in range(3):
    list[i]=1
print(list)

#크기가 100인 리스트 생성, 10개는 1로 채우시오.
#랜덤으로 섞어서 출력하시오.

list=[0]*100
for i in range(10):
    list[i]=1
random.shuffle(list)
print(list)


alist=[0 for i in range(100)]
print(alist)
for i in range(10):
    alist[i]=1
    
print(alist)#파괴
random.shuffle(alist)
print(alist)

#[10*10]2차원 배열을 생성하시오.(다시)

newLists=[["좌표"]*10 for _ in range(10)]