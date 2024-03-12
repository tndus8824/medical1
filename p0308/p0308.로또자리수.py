import random

lotto=str(random.randint(10000,99999))
print('\t[ 랜덤숫자 맞추기 ]')
print('랜덤숫자 : ',lotto)
a=input('5자리 숫자 입력\n --> ')
# 숫자 자리로 확인해서 맞춘갯수 출력
count=0
for i in range(len(lotto),0,-1):
    if a[i-1]!=lotto[i-1]:
        break
    else:
        if a[i-1]==lotto[i-1]:
            count+=1
            
print("맞는 개수 : ",count)
if count==0:
    print('꽝')
elif count==1:
    print('당첨숫자: {}\n 끝에서 {}개 당첨'.format(lotto,count))
elif count==2:
    print('당첨숫자: {}\n 끝에서 {}개 당첨'.format(lotto,count))
elif count==3:
    print('당첨숫자: {}\n 끝에서 {}개 당첨'.format(lotto,count))
elif count==4:
    print('당첨숫자: {}\n 끝에서 {}개 당첨'.format(lotto,count))
elif count==5:
    print('당첨숫자: {}\n 끝에서 {}개 당첨'.format(lotto,count))