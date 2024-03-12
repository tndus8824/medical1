stu1=[1,'홍길동',100,100,100,300,100.0,1]
stu2=[1,'유관순',90,90,90,270,90.0,2]
print('-'*35)
print('[학생성적프로그램]')
print('-'*35)
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생성적전체출력')
print('5.학생검색출력')
print('6.등수처리')
print('0.프로그램종료')
print('-'*35)

'''
#1번을 입력하면  학생성적입력을 선택했습니다
#만약 1번인 경우
# 이름,국,영,수
# stu3=[번호,이름,국,영,수,총,평,등]
#4번을 입력하면 학생성적출력을 선택했습니다

A=input("학생번호을 넣어주세요 >>>")
B=input("학생이름을 넣어주세요 >>>")
C=input("국어점수를 넣어주세요 >>>")
D=input("영어점수를 넣어주세요 >>>")
E=input("수학점수를 넣어주세요 >>>")
F=C+D+E
G=F/3
'''
member=[]
choice=int(input('원하는 번호를 입력하세요 >>'))
if choice==1:
    print("[학생성적입력]")
    for i in range(3):
        A=input("학생번호을 넣어주세요 >>>")
        B=input("학생이름을 넣어주세요 >>>")
        C=int(input("국어점수를 넣어주세요 >>>"))
        D=int(input("영어점수를 넣어주세요 >>>"))
        E=int(input("수학점수를 넣어주세요 >>>"))
        F=C+D+E
        G=F/3
        
        stu1=[A,B,C,D,E,F,G]
        member.append(stu1)
        print(member)
       
        
elif choice==4:
    print('학생성적출력')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수\t')
    for i in range(len(member)):
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2],
                                                      member[i][3],member[i][4],member[i][5],
                                                      member[i][6],member[i][7]))


4