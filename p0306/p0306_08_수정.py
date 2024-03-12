students=[{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]
cnt= len(students)+1  #학번  

while True:
    search=input("찾고자 하는 학생의 이름을 입력하세요 .(0취소)")
    chk=0
    if search =="0":
        break
    for s_dic in students:
        if s_dic["name"]==search:

            print(f"{search}학생을 찾았습니다.")
            chk +=1
            break
    print("찾고자 하는 학생의 위치 : ",chk)
    
    if chk !=len(students)-1:
        print(f"{search}학생을 찾았습니다.")
    else:
        print(f"{search}학생은 없습니다. 다시 입력하세요 ")
          
