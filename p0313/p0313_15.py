card_num = [0] * 13
for i in range(13):
    card_num[i] = i+1
card_num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
import random
# 랜덤으로 2개의 숫자를 뽑아서 출력하라
choice = random.sample(card_num,k=2)
print(choice)
print(f'랜덤숫자 : {choice[0]} -> {choice[0]-1}번 방에 있습니다.')
print(f'랜덤숫자 : {choice[1]} -> {choice[1]-1}번 방에 있습니다.')
if choice[0] > choice[1] :
    print(f"큰 수 : {choice[0]} , 작은 수 : {choice[1]}")
else :
    print(f"큰 수 : {choice[1]} , 작은 수 : {choice[0]}")