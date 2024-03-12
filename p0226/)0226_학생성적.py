
for i in range(5): #for 를 사용해서 5번 반복
    
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1.학생성적입력')
    print('4.학생성적전체출력')
    print('0.프로그램 종료')
    print('-'*35)
    ch =input('원하는 번호를 입력 하세요 >>> ')

    
    # if 문을 사용해서 1누르면 [학생성적입력]
    # 4 누르면 [학생성적전체출력]
    # 0 누르면 [프로그램 종료]
    
    if ch =='1' :
        print('[학생성적입력]')
        #이름,국,영,수 점수를 입력받아
        student=[]
        name=input("이름 >>> ")
        kor=int(input("국어점수 >>> "))
        eng=int(input("영어점수 >>> "))
        math=int(input("수학점수 >>> "))
        print('{}{}{}{}'.format(name,kor,eng,math))
        student=[name,kor,eng,math]
        print(student)   
    elif ch =='4':
        print('[학생성적전체출력]') 
        student=[]
        for i in range(len(student)):
            
            print('{}'.format(student[i]))
            print(student)
    
        

    print('*'*35)
    print('*'*35)