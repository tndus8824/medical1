students = []
#찾아서 수정하는 부분 다시 보충해서 적어두기
while True:
    # 찾는 부분 프로그램 작성하시오.
    search = input("찾는학생의 이름을 입력하세요.(0.취소)")
    chk = 0
    if search == "0":
        break
    for s_dic in students: #5명이 있으면 5번반복
        if s_dic["name"] == search:
            break
        chk += 1
    print("찾고자 하는 학생의 위치 :",chk)
#찾아서 삭제
if search =='0':
    break
for s_dic in students:
    if s_dic["name"] == search:
        break
    chk+=1
    
print("찾고자 하는 학생의 위치",chk)

if chk>=len(students):
    print("찾고자 하는 학생이 없습니다.")

else:
    print("{}학생을 찾았습니다.".format(search))
    s_input=input("{}학생 성적을 삭제하시겠습니까?(0.취소)".format(search))  
    #삭제
    if s_input =="1":
        print("삭제를 취소합니다")
        break
    
    else:
        del students[chk]
        print("{}학생 성적이 삭제되었습니다.".format(search))  