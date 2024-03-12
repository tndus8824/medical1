import random
#5*5 2차원 리스트를 0으로 채워서 출력하시오.
num=[0]*25
for i in range(5):
    num[i]=1
random.shuffle(num)
print(num)
4.#5*5 1차원 num이 2차원 리스트에 넣기
check_list=[[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        check_list[i][j]=num[5*i+j]
print(check_list)

5.#추첨판 만들기 5*5 
view_list=[['추첨']*5 for i in range(5)]
print(view_list)
cnt=1
answer_cnt=0
6.#checklist만들기
while True:
    
    print("\t[ 5*5 checkList 좌표 ]")
    print("-"*50)
    print("",0,1,2,3,4,sep="\t")
    print("-"*50)
    for i in range(5):
        print(i,end='\t')
        for j in range(5):
            print(check_list[i][j],end='\t')
        print() #나와줘야해!!!
        
    print("\t[ 5*5 당첨List 좌표 ]")
    print("-"*50)
    print("",0,1,2,3,4,sep="\t")
    print("-"*50)
    for i in range(5):
        print(i,end='\t')
        for j in range(5):
            print(view_list[i][j],end='\t')
        print()   
        
    #x,y좌표 입력하기
    print("{}번째 시도".format(cnt))
    x=int(input("x좌표를 입력하세요 >>>"))
    y=int(input("y좌표를 입력하세요 >>>"))
    if check_list[x][y]==1:
        view_list[x][y]="[당첨]"
        answer_cnt+=1 #당첨횟수
    else:
        view_list[x][y]="[꽝]"
        cnt+=1
        
    if answer_cnt ==5:
        print("[모두당첨] 프로그램종료")
        break
    if cnt ==11:
        print("[모든도전] 종료")
        break
        
      
        
 

# 5개의 당첨을 맞추면 프로그램 종료 anwer_cnt
 
 #10번 시도후 전체프로그램 종료 cnt=
    

    