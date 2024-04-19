a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#리스트 공간초기화를 먼저 해줘야 함
#a=[[0]*5]*5 #얕은복사
a=[[0]*5 for _ in range(5)] #컴프리헨션

value=1
for i in range(0,5): #0,1,2,3,4
    for j in range(0,5): #0,1,2,3,4
        a[i][j]=value #(5*i)+j+1
        value+=1
print(a) 
       
#좌표를 입력하면 좌표를 0으로 변경하는 프로그램을 구현
while True:
    #2차원 리스트 출력
    print(0,"ㅣ",0,1,2,3,4,sep='\t')
    print('-'*50)
    for i in range(0,5):
        print(i,"\t","ㅣ",end="\t")
        for j in range(0,5):
            print(a[i][j],end='\t')
        print()  
         
    x=int(input("X좌표를 입력하세요"))
    y=int(input("y좌표를 입력하세요"))
    print("{},{}".format(x,y))
    a[x][y]= 0     

  
