#함수선언
def plus(n1,n2): #def이름 (매개변수1,매개변수2)
    result=0
    result=n1+n2
    print("결과값: " ,result)

print("프로그램을 실행합니다.")

plus(1,2)# 매개변수가 2개면 무조건 2개 들어와야 함.아니면 에러
plus(10,20)# 함수호출: 함수이름(매개변수를 맞춰주면 됨)

n1,n2=1,2
result=0
result=n1+n2
print("결과값:",result)

n1,n2=10,20
result=0
result=n1+n2
print("결과값:",result)



#반복되는걸 짧게 쓰이게끔-> 함수사용