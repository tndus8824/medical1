#student =['k1','k2','k3']
students=[]

#이름,국어,영어,수학,합계,평균 입력하는 프로그램
count=1
while True:
    chk=input("학생성적을 추가하시겠습니까?(1.추가,0.취소)")
    if chk =="1":
        student={}
        #프로그램을 구현하시오.
        stuNo="k"+"{:03d}".format(count)
        count+=1
        name=input("이름을 입력하세요.>>")
        kor=int(input("국어점수를 입력하세요 >>>"))
        eng=int(input("영어점수를 입력하세요 >>>"))
        math=int(input("수학점수를 입력하세요 >>>"))
        total=kor+eng+math
        avg='{:.2f}'.format(total/3)
        print("학번이 추가되었습니다.")
        student["stuNo"]=stuNo
        student["name"]=name
        student["kor"]=kor
        student["eng"]=eng
        student["math"]=math
        student["avg"]=avg
        #최종 저장은 리스트에 딕셔너리를 저장
        students.append(student)
        print("[입력한 학생정보내역]")
        for k in student.keys():
            print("{}:{}".format(k,student[k]))
        print("-"*50)
        print(students)
        count+=1
    
    else:
        print("학번추가를 종료합니다")
        break
    


