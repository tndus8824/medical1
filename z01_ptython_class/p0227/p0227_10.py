'''
num=[]
#for문을 사용해서 1-10까지 숫자를 채우세요


print(num) #[1,2,3,4,5,6,7,8,9,10]

num2=[]
# 1-10까지 짝수를 num2리스트에 넣으세요

print(num2) #[2,4,6,8,10]

'''
'''
num=[]
for i in range(1,11):
    num.append(i)
print(num)

#한 줄로 표현 할 수도 있다.
num1=[i for i in range(1,11)]
print(num1)

num2=[]
for i in range(1,11):
    if i % 2 == 0:
        num2.append(i)
        
print(num2)

#1 ~ 10까지의 합 for문을 사용해서 구할 수 있음.
num=[1,2,3,4,5,6,7,8,9,10]
#num리스트를 사용해서 1-10까지의 합을 구해보세요
'''
sum=0
for i in range(1,11):
    num=[]
    num.append(i)
    sum+=i
print(sum)

#num2리스트 내 숫자들의 합을 구하세요
sum=0
for i in range(1,11):
    if i %2==0:
        num2=[]
        num2.append(i)
        sum+=i
print(sum)
