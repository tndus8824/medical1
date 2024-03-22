import operator
fruits = [
    "apple","banana","kiwi","pear","peach",
    "apple","apple","kiwi","kiwi","peach", "peach",
    "apple","pear","apple","apple","pear","pear","pear",
     "peach", "banana","banana"    ]
# numbers={1,2,3,4,5,5,6,7,4,3,2,12,67,8,9}
# counter={}

# for n in numbers:
#     if n not in counter:
#         counter[n] =0
#     counter[n]+=1
    
# print(counter)

counter={}
for n in fruits:
    if n not in counter:
        counter[n]=0
    counter[n]+=1
print(counter)
print(counter.items())
#items의 0번째 값을 가지고 순차정렬
sorted(counter.items(),key=operator.itemgetter(0))
#items의 역순정렬
sorted(counter.items(),key=operator.itemgetter(0),reverse=True)
#items의 1번째 값을 가지고 순차정렬
sorted(counter.items(),key=operator.itemgetter(1))
#items의 1번째 값을 가지고 역순정렬
sorted(counter.items(),key=operator.itemgetter(1),reverse=True)

