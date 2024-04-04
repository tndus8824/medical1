def sum(num1,num2):
    return num1+num2

num1=int(input("숫자를 입력하세요 >>"))
num2=int(input("숫자를 입력하세요 >>"))

print("두수의 합:  ",sum(num1,num2))
#자바는 전체를 읽어서 출력해서 함수의 위치가 위아래 상관 없지만
#파이썬은 순차적으로 읽어오기 때문에 함수의 위치가 위에 있어야 
#출력이 가능하다.
#CSS도 위에서 아래로 내려온다