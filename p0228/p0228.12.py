'''
주석 여러줄 쓸때

한줄 주석 #주석
# control+/ :커서 있는 문장 주석
# tab: 들여쓰기
# shift+ tab(들여쓰기 삭제)
# alt+ shift+ 위아래 방향키(커서 있는 문장 복사)
# '''
'''
a = 1
b = 2
c = 3

num=[100,200,300,400]
# for 문을 사용해서 하나씩 출력해보세요 2가지 방법 다 쓰기

for i in range(len(num)):
    print(num[i])

for i in num:
    print(i)
    
numlist=[[1,2][3,4][5,6]] # [1,2] #[3,4] #[5,6]
#             [num[0][0],num[0][1]],[num[1][0],num[1][1]],
for n in numlist:
    for a in n:
        print(a,end=' ')
    print()
# in range
for i in range(len(numlist)):
    print(i) #i=0,1,2
    print(numlist[i])
    for j in range(len(numlist[i])):
        print(numlist[i][j],end=' ')
    print()
    
'''
'''
f=[['딸기',100,1000],['수박',100,500],['사과',100,1200],['귤',100,300]]

#요소 한개한개를 출력해보세요

for i in f:
    for j in i:
        print(j,end=' ')
    print()

for i in range(len(f)):
    for j in range(len(f[i])):
        print(f[i][j],end=' ')
        #i=0 .j=0,1,2,
        #i=1. j=0,1,2
        #i=2  j=0,1,2
    print()

'''
score=[90,80,70,100,95,95,100]
total=[]
#점수의 총합을 구하세요
sum=0
for s in score:
    sum=sum+s
print(sum)
sum1=0
for i in range(len(score)):
    print(i)
    print(score[i])
    sum+=score[i]
print(sum1)

total.append(sum)   
print(total)