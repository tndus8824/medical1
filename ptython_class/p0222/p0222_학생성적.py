print('-'*35)
print('\t[학생성적프로그램]')
print('-'*35)
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생성적전체출력')
print('5.학생검색출력')
print('6.등수처리')
print('0.프로그램종료')
print('-'*35)

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}  \t{}'.format(
     1,'홍길동',100,100,100,300,100.0,1
))


print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}  \t{}'.format(
     1,'유관순',90,100,90,(90+100+90),(90+100+90)/3,1
))

print('-'*35)
print('\t[학생성적프로그램]')
print('-'*35)
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생성적전체출력')
print('5.학생검색출력')
print('6.등수처리')
print('0.프로그램종료')
print('-'*35)

stu_name1=input('첫번째 학생이름을 입력하세요 >>')
kor1=int(input("국어:  "))
eng1=int(input("영어:  "))
math1=int(input("수학:  "))
total=kor1+eng1+math1
avg1=(kor1+eng1+math1)/3

num=1
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{} \t{} \t{} \t{}  \t{}   \t{}  \t{}'.format(
     num,stu_name1,kor1,eng1,math1,total,avg1,1
))

num=num+1
stu_name2=input('두번째 학생이름을 입력하세요 >>')
kor2=int(input("국어 : "))
eng2=int(input("영어 : "))
math2=int(input("수학 : "))
total2=kor2+eng2+math2
avg2=(kor2+eng2+math2)/3
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{} \t{} \t{} \t{}  \t{}   \t{:.2f}  \t{}'.format(
     num,stu_name2,kor2,eng2,math2,total2,avg2,2
))

