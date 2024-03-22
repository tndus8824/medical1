#리스트(방법1)
num=[]
for i in range(1,11):
    num.append(i)
    print(num)
#컴프리핸션(방법3)
list=[i for i in range(1,11)]

#리스트(방법2) #방을 먼저 만드는거라 빠름.
list=[0]*10
for i in range(0,10):
    list[i]=i+1
print(list)