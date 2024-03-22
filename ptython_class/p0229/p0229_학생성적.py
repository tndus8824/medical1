cnt=0
members=[]
while True:#입력>출력>검색>삭제>수정
    print('_'*35)
    print('\t'+'[학생성적프로그램]')
    print('1.학생성적입력')
    print('2.학생성적수정')
    print('3.학생성적삭제')
    print('4.학생성적전체출력')
    print('5.학생검색출력')
    print('6.등수처리')
    print('0.프로그램종료')
    print('-'*35)
    ch=int(input('원하는 번호를 입력하세요 >>> '))
    if ch ==1:
        print('1.학생성적입력을 선택하였습니다')
        name=input('학생이름을 입력하세요>>> ')
        kor=int(input('국어점수를 입력하세요>>> '))
        eng=int(input('영어점수를 입력하세요>>> '))
        math=int(input('수학점수를 입력하세요>>> '))
        total=kor+eng+math
        avg=total/3
        cnt=cnt+1
        print('순서\t이름\t국어\t영어\t수학\t총합\t평균\t순위')
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(cnt,name,kor,eng,math,total,avg,1))
        stu=[cnt,name,kor,eng,math,total,avg,1]
        members.append(stu)
        print(members)
        
    elif ch==2:
        print('2.학생성적수정을 입력하였습니다.')  
    elif ch==3:
        print('3.학생성적삭제를 선택하였습니다.')   
    elif ch==4: 
        print('4학생성적전체출력을 선택하였습니다.')  
    elif ch==5:   
        print('5.학생검색출력을 선택하였습니다') 
    elif ch==6:  
        print('6.등수처리를 선택하였습니다') 
    elif ch==0: 
        print('0.프로그램종료를 선택하였습니다.')  
        break
