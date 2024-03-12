
score=[[80,90,85],[70,80,90],[84,92,80],[72,81,76]]
name=['홍길동','유관순','이순신','김구']
total=[]
#2.코딩
#2-1) 요소 하나하나 출력해보세요

for i in score:
    for j in i:
        print(j)
#2-2) 작은 요소의 합을 구해서  total 넣어주세요
sum=0
for i in range(len(score)):
    sum=0
    print(score[i])
   #i=0 ,score[0][0] +score[0][1]+score[0][2]
   #i=1 ,score[1][0] +score[1][1]+score[1][2]
   #i=2 ,score[2][0] +score[2][1]+score[2][2]
    for j in range(len(score[i])): 
        sum=sum+score[i][j]
        print(score[i][j])
    total.append(sum)
        
print(total)

#3-1)total출력

#3-2 )250미만 불합격 250이상 합격 ex)홍길동님 합격입니다.출력
for i in range(4):
    if total[i]>=250:
        print('{}님 합격입니다.'.format(name[i]))
    else:
         print('{}님 불합격입니다.'.format(name[i]))


