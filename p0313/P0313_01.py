#함수선언 def 이름() 정의
#함수값은return
#함수호출 이름 ()
#매개변수: 함수로 데이터전달하는 변수,매개변수 개수는 항상 같아야 한다.
#가변매개변수선언 *values, 가변매개변수는 일치하지 않아도 된다.
#리스트, 딕셔너리는 매개변수는 주소값이 전달이 된다.


#퀴즈1.
#함수를 사용하여 두수를 입력받아, 더하기,빼기,곱하기 ,나누기 결과값을 출력하시오.
# 두수입력을 받아 값을 리턴 받은 다음, 출력하시오.

#입력값(1)->함수(2)->출력(3)
#함수(2)을 출력으로 던져주기->입력값(1)->함수값을 받아 출력(3)
def cal(num1,num2):
    result1=num1+num2
    result2=num1-num2
    result3=num1*num2
    result4=num1/num2
    return result1,result2,result3,result4
A=int(input("첫번째 숫자를 입력해주세요"))
B=int(input("두번째 숫자를 입력해주세요"))

result1,result2,result3,result4=cal(A,B)
print("두수의 더하기",result1)
print("두수의 빼기",result2)
print("두수의 곱하기",result3)
print("두수의 나누기",result4)

    
#두수입력 받아 값을 리턴 받은 다음, 출력하시오.

#함수를 출력으로 던져주기
def cal(num1,num2,c):
    if c=="1":
        result1=num1+num2
    elif c=="2":
        result2=num1-num2
    elif c=="3":
        result3=num1*num2
    elif c=="4":
        result4=num1/num2
        return result1,result2,result3,result4
#입력
A=int(input("1번째 숫자를 입력하세요"))
B=int(input("2번째 숫자를 입력하세요"))
c=input("원하는 사칙연산을 입력하세요")
print("1.+ 2.- 3.* 4./")
#던져준 리턴값을 받음
result1,result2,result3,result4=cal(A,B,c)
#출력
print("{},{}결과값:{},{},{},{} ".format(A,B,result1,result2,result3,result4))