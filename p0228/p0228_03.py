#입력 : 이름, 점수(input)['홍길동',90]
#총 3명의 정보를 member리스트에 넣으세요

#print(member) #[['홍길동',90],['유관순'91]]

'''
member=[]
for i in range(3):
    name=input("이름을 입력하세요 >>> ")
    score=int(input("점수를 입력하세요 >>> "))
    a=[]
    a.append(name)
    a.append(score)
    member.append(a)
    
print(member)
'''
'''
#60점 이상이면 이면 홍길동님 불합격입니다.유관님 합격입니다.\
#[['홍길동',90],['유관순'91]]
member= [['홍길동',90],['유관순',91],['이순신',40]]

for i in range(3):
    name=member[i][0]
    score=member[i][1] #변수로 다시 설정해서 해도 됨
    
    if member[i][1]>= 60:
        print('{}님 합격입니다.'.format(member[i][0]))
    else:
        print('{}님 불합격입니다.'.format(member[i][0]))
   '''
   
#1부터 100까지의 합
'''
t=0
for i in range(1,101):
    t+=i
print('1부터 100까지의 합: {}'.format(t))

#1부터 100까지의 짝수의 합
sum=0
for i in range(1,101):
    if i %2==0:
        sum+=i
print('1부터 100까지의 짝수의 합:{}'.format(sum))
#1부터 100까지의 홀수의 합
n=0
for i in range(1,101):
    if i %2==1:
        n+=i
print('1부터 100까지의 홀수의 합:{}'.format(n))
'''
#1-10까지의 합 (오류수정)
sum=0
for i in range(1,11):
    sum+=i
print(sum)

num=[1,2,3,4,5,6,7,8,9,10]
#num리스트 안에 있는 값들의 합

n=0
for i in num:
    n+=i
print(n)

t1=0
for i in range(len(num)):
    print(num[i])
    t1+=i
print(t1)
