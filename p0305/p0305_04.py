##[[1,2,3,4,5],
# [6,7,8,9,10],
# [11,12,13,14,15],
# [16,17,18,19,20],
# [21,22,23,24,25]]


#.1-25 까지 리스트 생성
'''
from random import*
lotto=[] #변수선언
mynum=[] #입력받은 숫자 6개
num=[1,2,3,4,5,6,7,8,9,10]
for i in range(100):
    tmp=randint(0,9)
    print(tmp)
    num[0],num[tmp]=num[0],num[tmp]
    print(num)

for i in range(6):
    lotto.append(num[i])
print(lotto)

ok=[]
for i in range(len(mynum)):
    print(mynum[i])
    if mynum[i] in lotto:
        ok.append(mynum[i])
'''