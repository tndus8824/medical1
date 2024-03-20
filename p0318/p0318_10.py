class Card:
    def __init__ (self,kind,number):
        self.kind=kind
        self.number=number
    
    
 #리스트 선언
# c_list=[]
# kind=["spade","diamond","heart","clover"]
# number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
# for i in range(4):
#     for j in range(13):
#         c=[kind[i],number[j]]
#         c_list.append(c)

        
# for i in range(4):
#     for j in range(13):
#         print("카드출력: ",kind[i],number[j])

#클래스를 이용해서 52장의 카드 생성
c_list=[]
kind=["spade","diamond","heart","clover"]
number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(4):
    for j in range(13):
        c=Card(kind[i],number[j])
        #c=[kind[i],number[j]]#클래스를 생성해서 리스트레 추가
        c_list.append(c)
        
        
for i in range(52):
    print("카드 출력",c_list[i].kind,c_list[i].number)
    
    
    


#c1에 숫자를 5로 변경하시오
#c1을 출력하시오

#1개 변수 선언 -------------------
# kind="spade"
# number='1'

# kind="heart"
# number='5'

# kind="diamon"
# number='4'




#c2"heart","A"
#모양을 diamond로 변경후 출력하시오.

