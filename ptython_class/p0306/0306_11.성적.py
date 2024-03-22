# students = []
# students = [
#     {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
#     {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
#     {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
#     {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
#     {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
#     ]
#학생성적입력부분 구현하시오
    # 1. 학생성적입력 프로그램
'''
if choice==1:
    while True:
        name=input(f"{len(students)+1}번째 학생의 이름을 입력하세요.(0.취소)")
        
        if(name=="0"):
            print("학생 입력을 취소합니다.")
            break
        student={}#데이터 초기화
        student["stuNo"]="S"+"{:03d}".format(cnt)
        student["name"]=name #딕셔너리 추가
        #딕셔너리 추가
        
        kor=int(input("국어점수를 입력하세요 "))
        student["kor"]=kor #딕셔너리 추가
        eng=int(input("영어점수를 입력하세요 "))
        student["eng"]=eng #딕셔너리 추가
        math=int(input("수학점수를 입력하세요 "))
        student["math"]=math #딕셔너리 추가
        
        total=kor+eng+math
        student["total"]=total #딕셔너리 추가
        avg=total/3
        student['avg']=float('{:.2f}'.format(avg)) #딕셔너리 추가
        
        #list에 추가
        students.append(student)
        cnt+=1
        
        print("입력데이터 :",student)
        print(student) #list > dict
        print(students)
        
        
'''
#성적입력
cnt=1
student=[]
while True:
    name=input("첫번째 학생의 이름을 입력해주세요>>> ")
    students={}
    stuNo=int(input("학번을 입력하세요 >>> "))
    kor=int(input("국어점수를 입력하세요 >>>"))
    eng=int(input("영어점수를 입력하세요 >>>"))
    math=int(input("수학점수를 입력하세요 >>>"))
    student["stuNo"]="S"+"{:03d}".format(cnt)
    student["name"]=name
    student["kor"]=kor
    student["eng"]=eng
    student["math"]=math
    total=kor+eng+math
    student["total"]=total
    avg=total/3
    student["avg"]=float('{:.2f}'.format(avg))\
        
    students.append(student)
    cnt+=1
    print(student)
    print(students)
