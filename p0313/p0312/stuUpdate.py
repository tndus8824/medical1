import stuUpdate

def stu_print():
    print("[학생성적 프로그램]")
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적검색")
    print("4.학생성적수정")
    print("5.학생성적삭제")
 
 #성적점수부분 함수   
def s_update(s_title,choice,stu):
    print(f"[ {s_title[choice]}성적 수정 ]")
    print(f"현재 {s_title[choice]}점수 : {stu[choice+1]} ")
    print("-"*30)
    stu[choice+1] = int(input("수정 점수를 입력하세요."))
    print("수정된 점수 : ",stu[choice+1])
    stu[5] = stu[2]+stu[3]+stu[4]      # 합계수정
    stu[6] = float("{:.2f}".format(stu[5]/3)) # 평균수정
    print(f"{s_title[choice]}점수가 수정되었습니다." ) 