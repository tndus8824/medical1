import random

card_list = []
shape_list = ["spade","diamond","heart","clover"]
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = "A"
num_list[-3] = "J"
num_list[-2] = "Q"
num_list[-1] = "K"
# 카드 1세트 :52장 를 구현해서 출력하시오.
card_list = [[0]*2 for i in range(52)]

cnt = 0
for i in shape_list: # "spade","diamond","heart","clover"
    for j in range(13):
       card_list[cnt] = [i,num_list[j]]
       #print(card_list[cnt])
       cnt += 1
#카드를 랜덤섞기 print(card_list)
random.shuffle(card_list)

arr_num=0
while True:
    print("1.카드1장 뽑기")
    print("2.카드5장 뽑기")
    print("0.종료")
    print("현재 남은 카드:{} ".format(len(card_list)-arr_num))
    
    c_num=input("카드를 1개 뽑을까요? (1.[1장]뽑기)(2.[5장]뽑기)(3.[종료])")
    if c_num == 1:
        print(card_list[arr_num])
        arr_num+=1
        
    elif c_num ==2:
        for i in range(5):
            print(card_list[arr_num])
            arr_num+=1
            #1,2,3,4,5 /6,7,8,9,10

            
           
            
        
        
