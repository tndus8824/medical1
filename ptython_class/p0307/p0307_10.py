import random

fruit={'peach':'복숭아','orange':'오렌지',
       'apple':'사과','pear':'배','grapes':'포도',
       'mango':'망고','kiwi':'키위'}
print(fruit["peach"])
print(fruit["kiwi"])


# f_list=["peach","pear","kiwi"]
# print(fruit[f_list[0]])
# print(fruit[f_list[1]])
# print(fruit[f_list[2]])

# for f in f_list:
#     print(fruit[f])

f_list=list(fruit.keys())
print(f_list)

f_list_ran=random.sample(f_list,4)
print("랜덤추출: ",end="  :")
for f in f_list_ran:
    print(fruit[f])