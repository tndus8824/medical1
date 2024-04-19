
#리스트 만드는 방법(1)
a_list=[]
a_list.append(0) #리스트 append추가를 하게 되면 속도가 느림.
a_list.append(1)
a_list.append(2)
a_list[0]=3 # 리스트에 값을 넣는 것이 속도면으로 빠름.
print(a_list)

#공간을 만들어 놓고 for문을 돌림(2)
list=[0]*10
for i in range(10):
    list[i]=i+1
print(list)

#예시#
a = [[],[],[],[],[]]
value = 1
for i in range(0,5): #0,1,2,3,4
    for j in range(0,5): # 0,1,2,3,4
        a[i][j] = value  # (5*i)+j+1
        print(i,j,value)
        value += 1

print(a)   

#컴프리헨션을 사용하는 방법(3)
list1=[i+1 for i in range(10)]
#2차원 리스트 - 크기가 지정이 안됨.
