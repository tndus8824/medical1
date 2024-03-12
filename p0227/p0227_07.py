#1 - 5 까지의 합계를 구하세요

sum =1+2+3+4+5
total=0  #t=0
total=(0)+1 #t=1
total=(0+1)+2 #t=1+2
total=(0+1+2)+3 #t=1+2+3
total=(0+1+2+3)+4 #t=1+2+3+4
total=(0+1+2+3+4)+5 #t=1+2+3+4+5

#total=total+i
print(total)

t=0
for i in range(1,6,1):#i=1,2,3,4,5
    t=t+i
t=0
for i in range(1,6,1):#i=1,2,3,4,5
    t+=i
#1에서 10까지의 합을 구해보세요 for
sum10=0
for i in range(1,11):
    sum10=sum10+i
    print(i)
print('1부터 10까지의 합은 : {}입니다'.format(sum10))
#1에서 100까지의 합을 구해보세요for
#0+1
#0+1+2
#0+1+2+3

sum100=0
for i in range(1,101):
    sum100=sum100+i
print('1부터 100까지의 합은 :{}.입니다'.format(sum100))


#입력한 수부터 입력한 수 까지의 합을 구해보세요
sum=0
n1=int(input('첫번째숫자를 입력해주세요  > > >'))
n2=int(input('마지막숫자를 입력해주세요  > > >'))
for i in range(n1,n2+1):
    sum+=i
    #sum=sum+i
    
print('첫번째입력숫자: {} ~마지막입력 숫자: {} 까지의 합은 : {}'.format(n1,n2,sum))
    
