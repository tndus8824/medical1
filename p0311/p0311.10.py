
def cal(A,B):
    result1=A+B
    result2=A-B
    result3=A*B
    result4=A/B
    return result1,result2,result3,result4

A=int(input("1번째 숫자를 입력하세요 "))
B=int(input("2번째 숫자를 입력하세요 "))

result1,result2,result3,result4=cal(A,B)
data=cal(A,B)
print("더하기",result1)
print("더하기",result2)
print("더하기",result3)
print("결과값",result4)
print("결과값: ",result1,result2,result3,result4)
