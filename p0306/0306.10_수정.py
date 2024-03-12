
while True:
    print("[수정할 과목 선택]")
    print("-"*30)
    print("1.국어\t2.영어\t 3.수학")
    s_input=int(input("수정하려는 과목을 선택하세요 (0.취소)>> "))
    
    if s_input == 1:
        s_1 ="kor"
                         
    elif s_input == 2:
        s_2="eng"
      
    elif s_input ==3:
        s_3="math"
    
        
    else:
        print("과목 수정을 취소합니다.")
        break

#함수선언
def s_update(s_1):

