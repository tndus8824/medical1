#if -else
#if -elif -else
'''
if 조건문 1:
    실행문1
elif 조건문 2:
    실행문2
else:
    실행문3

조건문 1이면 참이면 실행문 1 실행 후 종료
조건문 1이 거짓이고 조건문2가 참이면 실행문 2 실행후 종료
조건문1, 조건문 2가 거짓이면 실행문3 실행 후 종료
'''
weather ='맑음'
if weather =='비':
    print('비가오네요 우산을 챙겨주세요')
elif weather == '눈':
    print('눈이옵니다 조심하세요')
else:
    print('선크림을 발라주세요')
    
# 변수가 양수이면 양수, 음수이면 음수, 0이면 0이라고 출력해보세요
num=-10

if num>0:
    print("양수")
elif num<0:
    print("음수")
else :
    print("0")

#돈이 만원이상[택시를탄다] 이천원이상[버스를 탄다]
#천원이상[따릉이를탄다] 나머지[걸어간다]
money =15000

if money>=10000:
    print("택시를 탄다")
elif 2000>= money:
    print("버스를탄다")
elif 1000>= money:
    print("따릉이를 탄다")
else:
    print("걸어간다")