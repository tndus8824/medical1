# print("a는 %s 입니다"%"입력값")
# a="입력값"
# print("a는 %s입니다"%a)
#입력함수 : input()=>문자열로 입력받는다.
# a= input("값을 입력해주세요 >>")
# print("a는 %s입니다"%a)

n1=input("첫번째 숫자를 입력하세요 >>")
n2=input("두번쨰 숫자를 입력하세요>>")
#문자열로 인식되어있다
print("두 수의 합 : ",n1+n2)
#문자를 숫자(정수)로 바꿔준다
#print("두 수의 합 (int형)":)
print("두 수의 합 : ",int(n1)+int(n2))
print("두 수의 합(float형): ",float(n1)+float(n2))

a=10 # 숫자
b="10" #문자
c=20 #숫자
d="20" #문자
print("숫자일 때 :" ,a+b)
print("문자일 때 :", b+d)