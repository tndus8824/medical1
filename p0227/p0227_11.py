from random import*
n1= randrange(1,10)
n2= randrange(10)
n3= randrange(1,10)
print(n1,n2,n3)


#lotto에 랜덤한 숫자 6개를 넣어보세요

lotto=[]
from random import*
for i in range(6):
    a=randint(1,10)
    lotto.append(a)

print(lotto)

#내가 직접 입력한 숫자 6개를 넣어보세요(for을 사용해서)

mynum=[]
for i in range(6):
    b=int(input(">> "))
    mynum.append(b)
print(mynum)




