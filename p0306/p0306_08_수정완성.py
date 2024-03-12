students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]

subject=['순번','학번','이름','국어','영어','수학','합계','등수']
s_title=['','국어','영어','수학']
cnt = len(students)+1 #학생이 5명인데 6명째 부터 입력을 해서~

while True:
    # 찾는 부분 프로그램 작성하시오.
    search = input("찾고자 하는 학생의 이름을 입력하세요.(0.취소)")
    chk = 0
    if search == "0":
        break
    for s_dic in students: #5명이 있으면 5번반복
        if s_dic["name"] == search:
            break
        chk += 1
    print("찾고자 하는 학생의 위치 :",chk)
    #못찾으면 다음단계로 넘어간다
    #(인덱스가 1이 증가되니까,전체길이만큼 돌렸는데 못찾으면 체크가 렌까지 올라감.)
    
    if chk == len(students):
        print(f"{search} 학생은 없습니다. 다시 입력하세요.")
    else:
        print(f"{search} 학생을 찾았습니다.")
        while True:
            print("[수정할 과목 선택]")
            print("-"*30)
            print("1.국어\t2.영어\t 3.수학")
            s_input=int(input("수정하려는 과목을 선택하세요 (0.취소)>> "))
         
            if s_input == 1:
                s_1 ="kor"
                print("[{}수정]".format[s_title[s_input]])
                print("현재{} 점수: {}" .format[s_title[s_input]],students[chk]["kor"])
                score=int(input("수정할 국어점수를 입력하세요. "))
                students[chk][s_1]=score
                
                #합계수정
                students[chk]["total"] = students[chk][s_1]+students[chk]["eng"]+students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))      
                print("{}점수: {}으로 수정이 완료되었습니다.".format(students[chk][s_1]))   
                print(students[chk])  
                                                            
            elif s_input == 2:
                s_2="eng"
                print("[{}수정]".format[s_title[s_input]])
                print("현재{}점수:{}" .format[s_title[s_input]],students[chk][s_2])
                score=int(input("수정할 영어점수를 입력하세요. "))
                students[chk]["eng"]=score
                #합계수정
                students[chk]["total"]=students[chk][s_1]+students[chk][s_2]+students[chk][s_3]
                students[chk]["avg"]=float("{:.2f}".format(students[chk]["total"]/3))      
                print("영어점수: {}으로 수정이 완료되었습니다.".format(students[chk][s_2]))   
                print(students[chk])   
                                      
            elif s_input ==3:
                s_3="math"
                print("[{}수정]".format[s_title[s_input]])
                print("현재{}점수:{}" .format[s_title[s_input]],students[chk][s_3])
                score=int(input("수정할 영어점수를 입력하세요. "))
                students[chk]["eng"]=score
                #합계수정
                students[chk]["total"]=students[chk][s_1]+students[chk][s_2]+students[chk][s_3]
                students[chk]["avg"]=float("{:.2f}".format(students[chk]["total"]/3))      
                print("영어점수: {}으로 수정이 완료되었습니다.".format(students[chk]["s_2"]))   
                print(students[chk])   
                      
                print("수학점수: {}으로 수정이 완료되었습니다.".format(students[chk][]))   
                print(students[chk])   
                
            else:
                print("과목 수정을 취소합니다.")
                break
                