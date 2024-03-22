class Car:#기본값 초기화
    car_name=""
    color=""
    door=0
    length=0
    width=0
    speed=0
    
    #생성자
    
    def __init__(self,car_name,color,door=5,length=1000,width=1000,speed): #매개변수(전받은값),위의 클랙스랑 다른변수
        self.car_name=car_name
        self.color=color
        self.door=door
        self.length=length
        self.width=width
        self.speed=speed
        
    def up_speed(self,s):
        self.speed+=s
        
#생성자를 사용한 객체선언 =인스턴트선언
c1=Car("드뉴아반떼","white",5,200,1000,60)  # 생성자를 호출한다. 
print("철수성능: ",c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)

c2=Car("드뉴아반떼","green",5,2000,1000,100)
print("영희성능: ",c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)

c3=Car("디올뉴그랜져","화이트펄",5,2500,1400,150)
print("반장성능: ",c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.speed)

        
#기본생성자를 사용한 객체선언       
# c1=Car()
# c1.car_name="드뉴아반떼"
# c1.color="white"
# c1.door=5
# c1.length=2000
# c1.width=1000
# c1.up_Speed(60)  #현재 speed에서 60을 더해줌
# c1.up_Speed(40)  #현재 speed에서 40을 더해줌
# c1.up_Speed(50)  #현재 speed에서 50을 더해줌
# c1.speed=50

# c2=Car()
# c2.car_name="드뉴아반떼"
# c2.color="green"
# c2.door=5
# c2.length=2000
# c2.width=1000
# c2.speed=100 
  
# c3=Car()
# c3.car_name="디올뉴그랜져"
# c3.color="화이트펄"
# c3.door=5
# c3.length=2500
# c3.width=1400 
# c1.up_Speed(150)



# #기본생성자를 사용한 객체선언
# c4=Car()
# c4.car_name="디올뉴그랜져"
# c4.color="화이트펄"
# c4.door=5
# c4.length=2500
# c4.width=1400 
# print("반장성능: ",c4.car_name,c4.color,c4.door,c4.length,c4.width,c4.speed)

# # print("철수성능: ",c1.car_name,c1.color,c1.door,c1.length,c1.width)
# print("영희성능: ",c2.car_name,c2.color,c2.door,c2.length,c2.width)
# print("철수성능: ",c3.car_name,c3.color,c3.door,c3.length,c3.width)

