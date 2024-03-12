# 두 수를 입력받아서 사칙연산을 출력해보세요
# 예: 30, 6을 입력받아서
# 출력 :
#30 + 6 = 36
#30 - 6 = 30
#30 * 6 = 180
#30 / 6 = 5.0

#변수를 사용해서 출력하기
a=30
b=6
print("%d+%d=%d"%(a,b,a+b))
print("%d-%d=%d"%(a,b,a-b))
print("%d*%d=%d"%(a,b,a*b))
print("%d/%d=%d"%(a,b,a/b))

#input 함수를 사용해서 출력하기
a=input("첫번째 숫자를 입력하세요 : ")
b=input("두번째 숫자를 입력하세요 : ")
print("%d+%d=%d"%(int(a),int(b),int(a)+int(b)))
print("%d-%d=%d"%(int(a),int(b),int(a)-int(b)))
print("%d*%d=%d"%(int(a),int(b),int(a)*int(b)))
print("%d/%d=%d"%(int(a),int(b),int(a)/int(b)))

#input 받은 문자전체를 int정수로 변환
a=int(input("첫번째 숫자를 입력하세요 : "))
b=int(input("두번째 숫자를 입력하세요 : "))
print("%d+%d=%d"%a,b,a+b)
print("%d-%d=%d"%a,b,a-b)
print("%d*%d=%d"%a,b,a*b)
print("%d/%d=%d"%a,b,a/b)