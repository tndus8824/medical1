def func1():
    a=20 #지역변수
    print("func1 a= ",a+10)
    #지역변수 값을 전역변수에 적용시키는 방법
    #코드를 추가하시오.
    return a
#전역변수의 값을 호출
def func2():
    global a # 전역변수를 가져옴
    a=100 #지역변수
    print("func2 b= ",a+10)
    
a=20 #전역변수
a=func1() #100
func2()
print("결과값: ",a)
