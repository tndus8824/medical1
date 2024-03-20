#랜덤으로 숫자 1개 생성
#입력한 숫자보다 크면 작은수를 입력하시오
#입력한 숫자보다 작으면 큰수를 입력하시오
#정답을 맞추면

#총 입력한 횟수 : 7회
#현재까지 입력한 숫자 : 1,5,7,6,8,4,50
#현재까지 입력했던 숫자를 모두 출력하시오

import random

ran_num=random.randint(1,100)
in_num=0
cnt=0
num_list=[]

while True:
    print("[랜덤숫자 맞추기 게임]")
    in_num = int(input("1-100 까지의 숫자를 입력하세요 >>"))
    num_list.append(in_num)
    if ran_num> in_num:
        print("입력한 숫자보다 큰수를 입력하세요 >> ")
    elif ran_num<in_num:
        print("입력한 숫자보다 작은수를 입력하세요>> ")
    else:
        print("정답입니다.")
        break 
    cnt+=1
    print("지금까지 입력한 횟수:{}회".format(cnt)) 
    print("현재까지 입력했던 숫자{}".format(num_list))