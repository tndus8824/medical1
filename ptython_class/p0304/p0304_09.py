students=[
    [1,'홍길동',100,100,99,299,99.97,1],
    [2,'유관순',99,99,98,296,98.67,1],
    [3,'이순신',80,80,81,241,80.33,1],
    [4,'김구',100,100,90,290,96.67,1],
    [5,'김유신',90,70,50,210,70.0,1],
    [6,'강감찬',100,100,100,300,100.0,1]
]
# 6
while True:
    #강감찬
    search = input("삭제하려고 학생의 이름을 입력하세요. ")
    # 이름찾기
    cnt=0 #찾는 학생의 위치
    #전체학생 검색
    for stu in students:
        if stu[1]==search:
            break
       
        cnt+=1
    if cnt == len(students):#전체학생수
        print("{}학생이 없습니다.".format(search))
    else:
        print("{}학생이 찾았습니다.".format(search))
        print("정말로 삭제하시겠습니까? ")
        del students[cnt]      
    print("찾은 위치 : ",cnt)
    
    print(students)
    print("-"*40)
    