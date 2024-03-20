class Card:#4개의 변수 :kind, number,width,height
    width=0 #클래스변수
    height=0 #클래스변수
    kind=""
    number=""
    def __init__(self,kind,number):#self는 클래스명,매개변수 해당X
        self.kind= kind
        self.number= number
        Card.width= 100
        Card.height= 200
        #카드의 크기는 동일하기 때문에 클래스 변수를 사용
 
 #클래스 5개를 생성해서 kind="spade",number=1,2,3,4,5
 #클래스를 출력하시오
 
 

card_list=[]
for i in range(13):
    card_list.append(Card("spade",i+1))
    

print("리스트 개수: ",len(card_list))

for i in range(13):
    print("리스트 출력: ",card_list[i].kind,card_list[i].number)
    
# print("리스트 출력: ",card_list[0].kind,card_list[0].number)

# a1=Card("spade","1")
# print(a1.kind,a1.number)

# a2=Card("spade","2")
# print(a2.kind,a2.number)

# a3=Card("spade","3")
# print(a3.kind,a3.number)

# a4=Card("spade","4")
# print(a4.kind,a4.number)

# a5=Card("spade","5")
# print(a5.kind,a5.number)
#1-13까지 넣어보세요
# card_list.append(Card("spade","A"))
# card_list.append(Card("spade","2"))
# card_list.append(Card("spade","3"))
# ...
# card_list.append(Card("spade","J"))
# card_list.append(Card("spade","Q"))
# card_list.append(Card("spade","K"))



 
 
 
 
 
 
 
 
 
        
#52장 카드 생성

shape=["SPADE","DIAMOND","HEART","CLOVER"]
number=["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_list=[]
for i in range(4):
    for j in range(13):
        c=Card(shape[i],number[j])
        card_list.append(c)

for i in range(52):
    c=card_list[i] #c=Card객체
    print("카드출력 : ",c.kind,c.number)
        
    
  


        