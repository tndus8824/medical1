student=[]

student=[[1,'홍길동',100,100,100,300,100.0,1], [2,'유관순',90,90,90,270,90.0,2]]
print('-'*35)
print('\t[학생성적프로그램]')
print('1.학생성적입력') #1명만 입력 print(student)
print('4.학생성적전체출력')#2명이 출력
print('-'*35)

ch = input('원하는 번호를 입력하세요 >>> ')
if ch == '1':
    print('[학생성적입력]')
    stu_name = input("이름을 입력하세요 >> ")
    kor = int(input('국어점수를 입력하세요 >> '))
    eng = int(input('영어점수를 입력하세요 >> '))
    math = int(input('수학점수를 입력하세요 >> '))
    
    stu3 = [3, stu_name,kor,eng,math,(kor+eng+math),(kor+eng+math)/3, 3]
    student.append(stu3)
    print(student)
    

    
elif ch == '4':
    print("[학생성적전체출력]")
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],student[0][5],student[0][6],student[0][7]))
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(student[1][0],student[1][1],student[1][2],student[1][3],student[1][4],student[1][5],student[1][6],student[1][7]))
else:
    print("잘못입력하였습니다.")
