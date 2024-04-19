#리스트를 사용해서 출력(다시)
stu1=[]

stu_num=input("이름을 입력해주세요>>>")
kor1=input("국어점수를 입력해주세요>>>")
eng1=input("영어점수를 입력해주세요>>>")
math1=input("수학점수를 입력해주세요>>>")
total1=kor1+eng1+math1
avg1=total1/3
stu1=[1,stu_num,kor1,eng1,math1,total1,avg1,1]
print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수\t')
print('{}{}{}{}{}{}{}{}'.format(stu1[0],stu1[1],stu1[2],stu1[3],stu1[4],stu1[5],stu1[6],stu1[7],stu1[8]))
stu_num2=input("이름을 입력해주세요")

stu1=[1,'홍길동',100,100,100,300,100.0,1]
stu2=[1,'유관순',90,90,90,270,90.0,2]
print('[학생 성적 출력]')
print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수\t')
print('{}{}{}{}{}{}{}{}'.format(1,stu_num,kor1,eng1,math1,total1,avg1,1))

