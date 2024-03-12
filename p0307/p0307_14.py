#컴프리핸션
list=[
    [0,0,0],[0,0,0],[0,0,0]
]

for i in list:
    for j in i:
        print(j,end="\t")
    
#[1차원 리스트] 1-9까지 숫자를 입력하세요
num=[]
for i in range(9):
    list.append(i+1)
print(num)

print(list)
list2=[2*n+1 for n in range(9)]
#n+1을 9번 반복해라.
print(list2)
#컴프리헨션
list3=[[n]*3 for n in range(3)]
print(list3)
#[2차원 리스트] 1-9까지 숫자를 입력하세요
#제곱근
numList=[num*num for num in range(1,6)]
print(numList)