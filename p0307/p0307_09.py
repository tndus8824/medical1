import random

fruit={'peach':'복숭아','orange':'오렌지',
       'apple':'사과','pear':'배','grapes':'포도',
       'mango':'망고','kiwi':'키위'}

print("개수",len(fruit))
#랜덤으로 4개출력-랜덤으로 4개를 추추
#랜덤은 리스트
#key는 리스트 타임으로 변경
print(fruit.keys())
print()
f_list=random.sample(list(fruit.keys()),4)
#4개의 랜덤 key를 출력하시오.
f_list2=["kiwi","grapes","peach","pear"]
print(fruit[f_list2][0])
print(fruit[f_list2][1])
print(fruit[f_list2][2])
print(fruit[f_list2][3])


#value 값을 전체출력
for key in fruit:
    print(fruit[key])