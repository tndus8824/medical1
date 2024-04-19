students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]
cnt=len(students)+1


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
    if choice==1:
        while True:
            name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
            if(name=="0"):
                print("학생 입력을 취소합니다.")
                break   
        student= {} #데이터 초기화
        student["stuNo"] = "S"+"{:03d}".format(cnt)
        student["name"] = name  # 딕셔너리 추가
        kor = int(input("국어점수를 입력하세요."))
        student["kor"] = kor
        eng = int(input("영어점수를 입력하세요."))
        student["eng"] = eng
        math = int(input("수학점수를 입력하세요."))
        student["math"] = math
        total = kor+eng+math
        student["total"] = total
        avg = total/3
        student["avg"] = float("{:.2f}".format(avg))
        # list에 추가
        students.append(student)
        cnt += 1 #학번증가
        print("입력 데이터 :",student) #list -> dict
        print(students)
    elif choice==2:
        print('\t[ 학생성적전체출력 ]')
        print('-'*65)
        print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
        print('-'*65)
        #[]에서 {}에 있는 키 값을 이중포문을 통해서 꺼내오는 법
        for s_dic in students:
            for s_key in s_dic:
                print(s_dic[s_key],end='\t')
            print()
        print()
            
    elif choice==3:
        search_students=[]
        print("학생이름검색을 선택하였습니다.")
        search=input("학생이름")
        search_cnt=0
        for s in students:
            if students["name"]==search:
                break
            search_cnt+=1
        if len(students) == search_cnt:
            print("찾는학생이 없다.다시검색해주세요")
        else:
            print("{}학생을 찾았습니다.")
        search_students.append(students[search_cnt])
        #0.이름을 입력
        #1.전체학생수에 있는 네임키 값에 이름이 있는지 없는지 확인(포문으로)
        #2.확인할때 마다 체크(chk)
        #3.체크한 학생수=전체학생수라면 검색한학생이 존재하지 않음
        #4.그렇지 않다면, 학생을 찾음
        #5.수정할 과목을 선택[국어,수학,영어]
        #6.현재값:{},수정값{}
        #7.수정값이 바뀌면 합계,총계가 바뀜
        #학생성적검색
        print("[ 학생성적 검색 ]")
        search = input("찾고자 하는 학생 이름을 입력하세요.>> ")
        # 검색한 이름으로 리스트에서 해당학생 검색
        search_cnt = 0
        for s in students:
            if s["name"] == search:
                break
            search_cnt += 1
        if len(students) == search_cnt:
            print("찾고자 하는 학생이 없습니다. 다시 검색하세요. ")
        else:
            print(f"{search} 학생을 찾았습니다.")
            s_title=["","국어","영어","수학"]
            chk=0
            while True:
                print("[ 수정할 과목 선택 ]")
                print("-"*30)
                print("1.국어\t2.영어\t3.수학")
                s_input = int(input("수정할려는 과목을 선택하세요.( 0.취소 ) >> "))
                if s_input == 1:
                    
                    s_1 = "kor"
                    print("[ {} 수정 ]".format(s_title[s_input]))
                    print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
                    print("-"*20)
                    score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
                    students[chk][s_1] = score
                    # 합계수정
                    students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                    students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                    
                    print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                    print(students[chk])
                    
                elif s_input == 2:
                    s_1 = "eng"
                    print("[ {} 수정 ]".format(s_title[s_input]))
                    print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
                    print("-"*20)
                    score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
                    students[chk][s_1] = score
                    # 합계수정
                    students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                    students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                    
                    print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                    print(students[chk])
                    
                elif s_input == 3:
                    s_1 = "math"
                    print("[ {} 수정 ]".format(s_title[s_input]))
                    print("현재 {}점수 : {}".format(s_title[s_input],students[chk][s_1]))
                    print("-"*20)
                    score = int(input("수정할 {}점수를 입력하세요.".format(s_title[s_input])))
                    students[chk][s_1] = score
                    # 합계수정
                    students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                    students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                    
                    print("{}점수 : {}점으로 수정이 완료되었습니다.".format(s_title[s_input],students[chk][s_1]))
                    print(students[chk])
                else:
                    print("과목수정을 취소합니다.")
                    break
            
    elif choice==5:
        print("학생성적삭제를 선택하였습니다.")
        pass
    elif choice==6:
        print("등수처리를 선택하였습니다.")
        for i in students:
            rank_cnt=1 # 순위 1을 기준
            for s in students:
                i["total"] > s["total"]
                rank_cnt+=1 #총합
            s["rank"]=rank_cnt #딕셔너리에 키값을 넣으면 추가적으로 넣어짐
        print("등수처리가 완료되었습니다.")
        print(students)
        
    elif choice==6:
        pass
    elif choice==7:
        break
    