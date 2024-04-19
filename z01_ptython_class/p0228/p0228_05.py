from random import *

#n1=randrange(1,11)
#n2=randint(1,10)

#랜덤한 숫자 4개 lotoo리스트에 넣고

lotto=[]
mynum=[]
for i in range(4):
    n1=randint(1,10)
    lotto.append(n1)
print(lotto)

#내가 입력한 숫자 6개는 mynum 리스트에 넣어주세요

for i in range(6):
    A= int(input("{}번째숫자를 입력해주세요 >>> ".format(i+1)))
    mynum.append(A)
print(mynum)

#로또 숫자 생성(랜던함 숫자 6개 lotto리스트에 넣고)
for i in range(6):
    n2=randint(1,10)
    #만약에 랜덤숫자 (n2)가 lotto리스트에 없다면
    if n2 not in lotto:
        lotto.append(n2)  #추가해라
print(lotto)

print('lotoo 숫자는 {}입니다'.format(lotto))
print('lotoo 숫자는 {}입니다'.format(mynum))
