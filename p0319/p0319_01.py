import random
#클래서 선언-설계도
class Card:
    
    def __init__(self,kind,number):
        self.kind=kind
        self.number=number

def random_one():
    num=random.randint(0,51)
    print("랜덤카드1장: " ,card_list[num].kind,card_list[num].number)

#52장의 카드 (2중포문)
#spade,diamond,heart,clover
#1,2,3,4,5,6,7,8,9,10,12,13
kind_list=["spade","diamond","heart","clover"]
number_list=[1,2,3,4,5,6,7,8,9,10,12,13]
card_list=[] #0부터 51번째 방



#52장의 카드생성
for i in range(4):
    for j in range(13):
        card_list.append(Card(card_list[i],card_list[j]))

#52장의 출력
for i in range(52):
    print("카드 : ",card_list[i].kind,card_list[i].number)
    
#랜덤으로 1장 뽑기 출력
random_one()
 
#중복을 하지 않고, 랜덤카드 5장 뽑으시오.
#1.0-51순차적인 것을 램덤 섞기 후,순차적으로 뽑으면 됨.
#2.5장을 랜덤으로 뽑으면 됨.
#1장뽑고 기존에 있는 카드와 비교해서 다시 뽑는 방법

#1.card_list shuffle
random.shuffle(card_list)
for i in range(5):
    print("랜덤섞기 카드: ",card_list[i].kind,card_list[i].number)

#2.card_list sample 5
print("2.card_list sample 5")
ran_list=random.sample(card_list,5)
for i in ran_list:
    print("랜덤섞기 카드: ",i.kind,i.number)
