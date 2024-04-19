import lotto1

lotto = [0]*45 #전체 45개 숫자
lucky_lotto =[0]*6 #당첨번호 6개숫자
my_lotto = [0]*6 #내가 입력한 6개 숫자
win_num=[]*6  #당첨된 번호 2개
win_amount=[0,0,1000,10000,1000000,100000000,10000000000]
#           0 1   2    3      4        5          6      (개 일치)


while True:
    choice = lotto1.screen()

    if choice==1:
        lotto1.num_generate(lotto)
    
    elif choice ==2:
        lotto1.num_shuffle(lotto) #번호섞기함수 호출
        
    elif choice ==3:
        lotto1.num_input(my_lotto) #3.나의 로또번호 입력
         
    elif choice==4:
        lotto1.num_check(lotto,my_lotto,lucky_lotto,win_num,win_amount)
        win_num=[] #초기화
        
        