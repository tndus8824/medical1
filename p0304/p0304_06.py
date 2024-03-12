students=[
    [1,"홍길동",100,100,99,299,99.97],
    [2,"유관순",100,100,99,299,99.97],
    [3,"이순신",100,100,99,299,99.97]
]

while True:
    search=input('찾는 학생의 이름을 입력하세요')
    chk=0
    count=0
    for stu in students:
        if search in stu:
            chk=1
            break
        count+=1 #찾는 학생 위치값
    if chk ==0:
        print("찾는 학생의 정보가 없습니다.")
    else:
        print("입력한 학생을 찾았습니다.")
        print("[변경할 과목 선택]")
        num=input("1.국어 2.영어. 3.수학")
        if num ==1:
            print("국어를 선택하셨습니다.")
        elif num ==2:
            print("영어를 선택하셨습니다.")
        elif num ==3:
            print("수학을 선택하셨습니다.")
        