# 리스트에 1, 25까지 숫자를 리스트에 입력하시오.
#[[1,2,3,4,5],[6,7,8,9,10].....[21,22,23,24,25]]

x = [[(5 * j)+ (i + 1) for i in range(5)] for j in range(5)]
print(x)
a=[]
for i in range(0,25):
    a.append(i+1)
print(a)

#1부터 25까지 2차원 리스트 생성
b=[]
b_i=[]
for i in range(0,25):
    if (i+1) %5 ==0:
        b_i .append(i+1)
        b.append(b_i)
        b_i=[]
        pass
    else:
        b_i.append(i+1)#[1,2,3,4]       
print(b)

