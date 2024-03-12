fruit={'peach':'복숭아','orange':'오렌지',
       'apple':'사과','pear':'배','grapes':'포도',
       'mango':'망고','kiwi':'키위'}

#복숭아 영어로 입력하시오.
#총 몇문제를 맞추었는지?
for f in fruit:
    eng_in=input("{}을 영어로 입력하세요 ".format(fruit[f]))
    print("입력한 단어 : {}".format(eng_in))
    if f==eng_in:
        print("정답입니다")
    else:
        print("{}가 정답입니다".format(f))

