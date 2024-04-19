#반복문
'''
for 변수 in range(시작값,끝값+1,증가값)
'''
'''
for i in range(3):# i=0,1,2
    print('안녕')
    #i= 0일때
    #i= 1일때
    #i= 2일때
    
for i in range(3): #i = 0 , 1 ,2
    print(i)
#i =0,1,2,3...
for i in range(100):
    print(i+1)

sum1=0
for i in range(1,6,1):
    sum=sum+i
'''
#숫자 한개를 입력받아서 1부터 입력한 수 까지의 합을 구하세요

n1=int(input('숫자를 입력해주세요 >>> '))
t=0
for i in range(1,n1+1):
   
    t=t+i

print('{}부터 입력한 수:{}까지의 합은: {}입니다'.format(1,n1,t))

#다시
#짝수의 합만 구함 (2+4+6+8+10+...)
n2=int(input('숫자를 입력해주세요 >>> '))
t=0 #짝수의 합을 넣을 변수
for i in range(1,n2+1):
    if n2 %2==0:
        t=t+i
        print(i)
print('{}부터 {} 까지의 짝수의 총합은: {}'.format(1,n2,t))