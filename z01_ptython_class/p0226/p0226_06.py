student=[]

#두명 이상의 학생의
#이름, 국, 영, 수 점수를 입력 받아
#리스트를 생성후,
#student리스트에 넣어주세요
#student리스트 전체 출력


name =input("첫번째 이름을 입력해주세요 >>>  ")
kor=int(input("국어점수를 입력해주세요 >>>  "))
eng=int(input("영어점수을 입력해주세요 >>>  "))
math=int(input("수학점수을 입력해주세요 >>>  "))
total=kor+eng+math
avg=total/3

name2 =input("두번째 이름을 입력해주세요 >>>  ")
kor2=int(input("국어점수를 입력해주세요 >>>  "))
eng2=int(input("영어점수을 입력해주세요 >>>  "))
math2=int(input("수학점수을 입력해주세요 >>>  "))
total2=kor2+eng2+math2
avg2=total2/3

print("이름\t국어\t영어\t수학\t총점\t평균")
print('{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(name,kor,eng,math,total,avg))
print('{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(name2,kor2,eng2,math2,total2,avg2))
student1=[] #빈리스트 만들기
student1.append(name)
student1.append(kor)
student1.append(eng)
student1.append(math)
student1.append(total)
student1.append(avg)
print(student1)

student2=[name2,kor2,eng2,math2,total2,avg2] #기본값세팅
print(student2)
