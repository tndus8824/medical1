students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]

cnt = len(students)+1
# 학생번호 사용
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue # 반복문 계속실행
    choice = int(choice)
    #학생성적입력
    if choice ==1:
        while True:
            student={}
            name=input(f'{len(students)+1}번째 학생이름을 입력해주세요>>(0.취소)')
            if(name==0):
                break
            student['stuNo']='S'+'{:03d}'.format(cnt)
            kor=int(input("국어점수>> "))
            student['kor']= kor
            eng=int(input("영어점수 >>"))
            student['eng']= eng
            math=int(input("수학점수>> "))
            student['math']= math
            total=kor+eng+math
            student['total']= total
            avg=total/3
            student['avg']= '{:.2f}'.format(avg)
            
            students.append(student)
            print("입력데이터 : ", student)
            print(students)
    #학생성적전체출력        
    elif choice==2:
        print("학생성적전체출력을 선택하였습니다.")
        print("학번\t이름\t국어\t수학\t영어\t총점\t평균")
        for s_dic in students:
            for s_key in s_dic :
                print(s_dic[s_key])
            print()
        print("-"*60) 
        
    
    elif choice==3:
        pass
    #학생검색,학생수정
    elif choice==4:
        s_title=['','수학','국어','영어']
        while True:
            search=input("수정할 학생의 이름을 입력>> 0.취소")
            chk=0
            if search =='0':
                break
            
            for s_dic in students:
                if s_dic['name']==search:
                    chk+=1
                print("찾고자 하는 학생의 위치",chk)
            if chk ==len(students):
                print("{search}를 찾지 못하였습니다.")
            else:
                print("{search}를 찾았습니다.")
                while True:
                    print("수정할 과목 선택 1.국어 2.수학 3.영어")
                    s_input=input("수정할 과목을 선택하세요>>(0.취소)")
                    if s_input == '1':
                        s_1='kor'
                        print("{}수정 :".format(s_title[s_input]))
                        print("현재{}점수:{} ".format(s_title[s_input],students[chk][s_1]))
                        score=int("수정할 {}점수를 입력하세요>>".format(s_title[s_input]))
                        students[chk][s_1]=score
                        #합계수정
                        students[chk]['total']=students[chk][s_1]+students[chk]['eng']+students[chk]['math']
                        students[chk]['avg']='{:.2f}'.format(students[chk]['total']/3)
                        print("{}점수: {}점수로 변경이 완료".format(s_title[s_input],s_title[chk][s_1]))
                        print(students[chk])
                    elif s_input =='2':
                        s_1='eng' 
                        print("{}수정".format(s_title[s_input]))
                        print("현재{}점수: {} ".format(s_title[s_input],s_title[chk][s_1]))   
                        score=int("수정할 {}점수를 입력하세요 >>".format(s_title[s_input]))
                        students[chk][s_1]=score
                        #합계수정
                        students[chk]['total']=students[chk]['kor']+students[chk][s_1]+students[chk]['eng']   
                        students[chk]['avg']='{:.2f}'.format(s_title[chk]['total']/3) 
                        print("{}점수:{}점수로 변경이 완료".format(s_title[s_input],s_title[chk][s_1]))    
                        print(students[chk])  
                    elif s_input =='3':
                        s_1='eng' 
                        print("{}수정".format(s_title[s_input]))
                        print("현재{}점수: {} ".format(s_title[s_input],s_title[chk][s_1]))   
                        score=int("수정할 {}점수를 입력하세요 >>".format(s_title[s_input]))
                        students[chk][s_1]=score
                        #합계수정
                        students[chk]['total']=students[chk][kor]+students[chk][eng]+students[chk][s_1]   
                        students[chk]['avg']='{:.2f}'.format(s_title[chk]['total']/3) 
                        print("{}점수:{}점수로 변경이 완료".format(s_title[s_input],s_title[chk][s_1]))    
                        print(students[chk])    
                    else:
                        print("과목수정을 취소합니다.") 
                        break    
    elif choice==5:#모름
        print("등수처리")
        for i,s_ic in enumerate(students):
            rank_cnt=1
            for i_dic in students: #i_dic은 새로운 리스트
                if s_dic["total"]<i_dic["total"]: #두수를 비교
                    rank_cnt += 1 # 현재 학생의 합계보다 크면 1증가
            s_dic["rank"] = rank_cnt
        print("등수처리가 완료되었습니다.")
        print(students)  
        
      
    elif choice ==6:
        print("학생삭제를 선택하였습니다.")
        while True:
            search=input("삭제할 학생의 이름을 입력>> 0.취소")
            chk=0
            if search =='0':
                break
            
            for s_dic in students:
                if s_dic['name']==search:
                    chk+=1
                print('찾고자 하는 학생의 위치',chk)
            s_input=input('{}학생의 이름을 삭제하겠습니까?(0.취소)'.format(search))
            if s_input !=1:
                print("삭제를 취소하였습니다.")
                break
                
            else:
                del(students[chk])
                print("{}학생의 성적이 삭제되었습니다.".format(search))            
              
        
                                     
                
                    
                

  
        
           
        