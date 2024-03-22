# n1 부터 n2까지의 합 구하는데
#n1=n2 비교해서 작은수를 n1에 넣기
'''
#<다시해보기>
n1=int(input('첫번째 숫자를 입력해주세요 >>  '))
n2=int(input('두번째 숫자를 입력해주세요 >>  '))
sum=0
for i in range(n1,n2+1):
    sum=sum+i
    
print(sum)
'''
#만약에 n1이 n2보다 크다면 둘의 값을 바꿔라
n1=0
n2=0
if n1>n2:
    n1,n2=n2,n1
#1.n1부터 n2까지의 합 구하는데
n1=int(input('첫번째 숫자를 입력해주세요 >>  '))
n2=int(input('두번째 숫자를 입력해주세요 >>  '))
sum=0
for i in range(n1,n2+1): #i=n 인거지?
    sum=sum+i
print(sum)

odd_list=[]
#3.n1-n2까지의 홀수 값을 저장
for i in range(n1,n2+1):
    if i %2==1:
        odd_list.append(i)
        
print(odd_list)        
