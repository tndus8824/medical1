# 해보세요

n1=24
n2=5

n1=int(input("첫번쨰 숫자를 입력해주세요 >>>"))
n2=int(input("두번쨰 숫자를 입력해주세요 >>>"))
       
cal =input('수식을 입력하세요 (+,-,*,/) >>  ')
if cal == '+':
    print('두수의 합은  >> {}'.format(n1+n2))
elif cal == '-':
    print('두수의 차는  >> {}'.format(n1-n2))
elif cal == '*':
     print('두수의 곱은  >> {}'.format(n1*n2))
elif cal == '/':
     print('두수의 나눈값  >> {}'.format(n1/n2))
else:
    print("잘못 입력하였습니다")