import random
import lotto1
#1.번호생성
#2.번호섞기
#3.번호뽑기
#4.번호확인
def screen():
    print("[로또번호 맞추기 프로그램]")
    print("1.번호생성")
    print("2.번호섞기")
    print("3.나의 로또번호입력")
    print("4.로또당첨번호확인")
    print("5.번호확인")
    print("-"*30)
    choice=int(input("원하는 번호를 입력하세요 >>"))
    return choice
#번호 생성함수
def num_generate(lotto):
     if choice ==1:
        print("[번호생성]")
        for i in range(45):
            lotto.append(i+1)
        # lotto=[i for i in range(1,46)]#지역변수로 변환, 새롭게 재정의
        print(lotto)
        #return lotto
#번호 섞기 함수
def num_suffle(lotto):
    print("[번호섞기]")
    random.shuffle(lotto)
    print(lotto)

def num_input(my_lotto):
    print("[나의 로또번호 입력]")
    for i in range(6):
        my_num=int(input(f'{i+1}번째 로또번호를 입력하세요. >>'))
        my_lotto[i]=my_num
    print("내가 입력한 로또 번호 :",my_lotto)
    
def num_check(lotto,my_lotto,lucky_lotto,win_num,win_amount):
    #win_num=[]이쪽에서 하면 안되유.지역변수인식이 되어서 주소값을 다시 세팅
    for i in range(6):
        lucky_lotto[i]=lotto[i]
    print(("[로또번호 확인]"))
    print("로또번호: ",lucky_lotto)
    print("내가 입력한 번호: ",my_lotto)
    #몇개 맞췄는지 확인소스
    for i in my_lotto: #1,20,21,23,25,44
        if i in lucky_lotto: #,1,20,21,23,25,44
            win_num.append(i) #
    print("당첨된 번호: ",win_num)
    #당첨금액 출력
    print("당첨금액 : {:,d} 원".format(win_amount[len(win_num)]))

#-----------------------------------------------------
lotto = [0]*45 #전체 45개 숫자
lucky_lotto =[0]*6 #당첨번호 6개숫자
my_lotto = [0]*6 #내가 입력한 6개 숫자
win_num=[]*6  #당첨된 번호 2개
win_amount=[0,0,1000,10000,1000000,100000000,10000000000]
#           0 1   2    3      4        5          6      (개 일치)


while True:
    choice=lotto.screen()

    if choice==1:
        lotto.num_generate(lotto)
    
    elif choice ==2:
        lotto.num_shuffle(lotto) #번호섞기함수 호출
        
    elif choice ==3:
        lotto.num_input(my_lotto) #3.나의 로또번호 입력
         
    elif choice==4:
        lotto.num_check(lotto,my_lotto,lucky_lotto,win_num,win_amount)
        win_num=[] #초기화
        
        
        
        
    
        
        
        