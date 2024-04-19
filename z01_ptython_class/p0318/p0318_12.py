#car 클래스를 선언해서 
#carCount클래스 변수
#carNo에는 carCount숫자를 이용해서 carNo를 넣으시오.
#carNo,color="white",door=5, tire=4 ,speed
#upspeed는 함수를 호출하면 10씩 증가
#downspeed는 함수를 호출하면 10씩 감소

#c1-1,white,5,4,0->speed 30이 되도록
#c2-2,red,5,4,0->speed 100이 되도록
#c3-3,silver,5,4,0->speed 70

#car_list 추가하고

#car_list 에 있는 모든 객체의 모든 color,door,tire,speed 모두 출력하시오.

class Car():
    stuCount=0#클래스 변수
    CarNo=0 #인스턴스변수
    def __init__(self,color="white",door=5, tire=4,speed=0):
        self.color=color
        self.door=door
        self.tire=tire
        self.speed=speed
        Car.stuCount +=1
        self.CarNo=Car.stuCount 
    def upspeed(self,sp):
        self.speed+=sp
        
    def downspeed(self,sp):
        self.speed-=sp
    
    def __str__(self):
        return(f'{self.CarNo},{self.color},{self.door},{self.tire},{self.speed}')
        
    
c1=Car("white",5,4,0)
for i in range(3):
    c1.upspeed(10)


c2=Car("red",5,4,0)
for i in range(10):
    c2.upspeed(10)

c3=Car("silver",5,4,0)
for i in range(7):
    c3.upspeed(10)


c_list=[c1,c2,c3]
print(c1.color,c1.door,c1.tire,c1.speed)
print(c2.color,c2.door,c2.tire,c2.speed)
print(c3.color,c3.door,c3.tire,c3.speed)

for i in c_list:
    print(i.color,i.door,i.tire,i.speed)
    

list=[["white",5,4,30],["red",5,4,100],["silver",5,4,70]]
for i in list:
    for j in i:    
        print(j,end="\t")
    print()
    