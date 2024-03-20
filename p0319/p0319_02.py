class Car:
    color =""
    door=5
    tire=4
    speed=0
    
    def __init__(self,color,door,tire,speed):
        self.color=color
        self.door =door
        self.tire =tire
        self.__speed=speed
        
    def up_speed(self):
        self.__speed+=10
    
    def down_speed(self):
        self.__speed-=10
        
    
c1=Car("white",5,4,0)
c1.up_speed()
print(c1.speed)
