#1 - 45 까지의 숫자를 넣어서(다시해보기)

from random import*
l=[]
lotto=[]
mynum=[]
#섞는거
ok=[]

#1.입력받은 숫자 6개
for i in range(6):
    n=int(input('{}번째 숫자를 입력하세요  >>>  '.format(i+1)))
    mynum.append(n)
print(mynum)


#2. 리스트에 1-45 중복이 없는 1-45까지의 숫자가 들어있음.(중복없이45개의 로또를 섞는것) 
for i in range(1,46):
    l.append(i)
 
for i in range(100):
    tmp=randint(0,44)
    l[0],l[tmp]=l[tmp],l[0]
    
#3.45개중에서 랜덤 6개 뽑기 (lotto)
for i in range(6):
    lotto.append(l[i])
print(lotto)

# 4.입력받은 숫자 6개와 랜덤숫자와 [비교]
for i in range(6):
    n=int(input('{}번째 숫자를 입력하세요  >>>  '.format(i+1)))
    mynum.append(n)
#입력숫자와 랜덤숫자 비교같은거 출력
#매치하는 숫자, 개수,
#m=[1,2,3] l=[3,6,7]
#lotto[1,2,3,4,5,6]
#mynum[7,8,9,10,11,12]

#5.입력받은 숫자와 랜덤숫자가 같으면 [출력]
ok=[]
for i in range(6):
    if mynum[i] in lotto:
        ok.append(mynum[i])
print(ok)
print('입력한 숫자 : {}'.format(mynum))        
print('로또 숫자: {}'.format(lotto))        
print('당첨된 숫자 : {}'.format(ok))        
        