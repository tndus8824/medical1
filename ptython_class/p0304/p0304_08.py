# #students=[
#     [S001,'홍길동',100,100,99,299,99.97,1],
#     [S002,'유관순',99,99,98,296,98.67,1],
#     [S003,'이순신',80,80,81,241,80.33,1],
#     [S004,'김구',90,70,50,210,70.0,1],
#     [s005,'강감찬',100,100,100,300,100.0,1]
# ]
# 등수처리
'''
    elif choice==5:
        while True:
            choice=input("등수처리를 실행하시겠습니까?(1.실행 0.취소)")
            if choice == "0":
                print("등수처리를 취소하셨습니다.")
                break
            else:
                #등수처리진행
                for i_stu in students:
                    no=1 #초기화
                    for j_stu in students:
                        #각각의 총합비교
                        if i_stu[5] < j_stu[5]:
                            no+=1
                    i_stu[7]=no #등수위치에 no 저장
            print("등수처리가 완료 되었습니다.")
            print("_"*40)
            print("[등수확인]")
            print(students)
            '''