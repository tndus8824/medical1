# students=[
#     [S001,'홍길동',100,99,87,286,95.33,2],
#     [S002,'유관순',98,93,87,278,92.67,3],
#     [S003,'이순신',88,76,30,194,64.67,5],
#     [S004,'김구',100,100,100,300,100.0,1],
#     [s005,'강감찬',98,85,44,227,75.67,4]
# ]

students=[{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]
cnt= len(students)+1     
count=0

while True:
    #학생을 먼저 찾아야 함.
    # 학생 찾는 프로그램을 입력하시오
    serchNo=input("학생전체를 출력을 하시겠습니까?(1.확인,2취소)")
    if count ==0:
        break
    print('[학생성적전체출력]')
    print('-'*55)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
    print('-'*55)
    for s_dic in students:
        for s_key in s_dic:
            print(s_dic[s_key],end='\t')
        print()
    