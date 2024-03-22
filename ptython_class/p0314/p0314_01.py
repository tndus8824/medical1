#예외구분
while True:
    #런타임 오류: 프로그램 실행 중에 발생하는 오류
    try:#오류가 발생 될것 같은 지점
        num=int(input("숫자를 입력하세요 >> "))
        a_list=[1,2,3,4,5]
        for i in range(num):
            print(a_list[i])
    except:
        print("구문에 오류가 났습니다.")
    

