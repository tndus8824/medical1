import random


a=[]
for i in range(0,25):
    a.append(i+1)
print(a)
random.shuffle(a)
print(a)
arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(0,5):
        for j in range(0,5):
            arr[i][j]=a[(5*i)+j]
print(arr)

#출력
while 1:
    print('-'*50)
    print("      [좌표맞추기 프로그램]")
    print("순번","ㅣ",0,1,2,3,4,sep="\t")
    print('-'*50)
    for i in range(0,5):
        print(i,"\t","ㅣ",end="\t")
        for j in range(0,5):
            print(arr[i][j],end="\t")
        print()
    print("-"*50)
    x=int(input("x좌표를 입력하세요. "))
    y=int(input("y좌표를 입력하세요. "))
    arr[y][x]='X'