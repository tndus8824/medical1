students=[
    [1,"홍길동",100,100,99,299,99.97],
    [2,"유관순",100,100,99,299,99.97],
    [3,"이순신",100,100,99,299,99.97]
]



#찾고자 하는 학생찾기
while True:
    
    search= input("검색하고 싶은 학생을 입력하세요 .(0.취소)")
    chk=0 #찾는 정보확인
    count= 0
    if search == '0':
        break
    for stu in students:
        if search in stu:#홍길동,유관순,이순신
            chk=1 #정보를 찾았을 때 정보를 1로 변경
            print("{}의 학생정보를 찾았습니다".format(search))
            break
        count+=1
        
    if(chk==1):
        #전체학생전체출력
        print("{}의 학생의 정보를 찾았습니다.".format(search))
        print("[학생성적 출력]")
        print("-"*60)
        print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
        print("_"*60)
        for i in students[count]:
            print(i,end="\t")
        print()
    else:
        print("찾는 학생이 없습니다.")
   
  