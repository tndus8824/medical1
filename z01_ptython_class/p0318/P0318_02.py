class Car:#기본값 초기화
    car_name=""
    color=""
    door=0
    length=0
    width=0
    speed=0
    
    def up_Speed(self,s):# 클래스내에 함수는 self라는걸 적어줘야한다.
        self.speed += s
        
c1=Car()
c1.car_name="드뉴아반떼"
c1.color="white"
c1.door=5
c1.length=2000
c1.width=1000
c1.up_Speed(100)  #현재 speed에서 100을 더해줌

c2=Car()
c2.car_name="드뉴아반떼"
c2.color="green"
c2.door=5
c2.length=2000
c2.width=1000
c2.speed=100 
  
c3=Car()
c3.car_name="디올뉴그랜져"
c3.color="화이트펄"
c3.door=5
c3.length=2500
c3.width=1400 
c1.up_Speed(150)

print("철수성능: ",c1.car_name,c1.color,c1.door,c1.length,c1.width)
print("영희성능: ",c2.car_name,c2.color,c2.door,c2.length,c2.width)
print("철수성능: ",c3.car_name,c3.color,c3.door,c3.length,c3.width)

