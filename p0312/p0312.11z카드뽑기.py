import random

#카드종류:SPADE,DIAMOND,HEART,CLOVER 4종류
#카드 숫자:A,2,3,4,5,6,7,8,9,10,J,Q,K 13장




def card_create():
    pass

            
def card_shuffle():
    pass

    
def card_share():
    pass

             
def card_print():
  
  pass
c_shape = ["spade","diamond","heart","clover"]    
c_number=[0]*13
for i in range(13):
    c_number[i]=i+1
c_number[0]="A"       
c_number[11]="J"      
c_number[12]="Q"       
c_number[13]="k"       

while True:
    print("[카드 프로그램]")
    print("1.카드생성")
    print("2.카드섞기")
    print("3.카드5장 나눠주기")
    print("4.카드5장 확인하기")
    print("0.종료")
    print("-"*40)
    choice=int(input("선택할 메뉴번호를 선택하세요>>>"))


    if choice ==1:
        print("카드생성")
        card_creat(num_list)
    elif choice ==2:
        print("카드섞기")
        card_shuffle(card_list)
    elif choice ==3:
        print("카드5장 나눠주기")
        card_share(card_list,num_list)
    elif choice ==4:
        print("카드5장 확인하기")
        card_print(card_list)
    else:
        print("프로그램을 종료합니다")
        break

    

