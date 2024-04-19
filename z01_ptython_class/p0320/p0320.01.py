class Car:
    count=10
    
    
    def __init__(self,color="",speed=0):#키워드 변수초기화
        self.color=color #init 안에 변수 선언 -인스턴스변수
        self.speed=speed
        
        
# class사용하기 위해서는 인스턴스 선언
c1=Car()#인스턴스 선언 
c1.color="white"# 매개변수 초기화 세팅해줘야 해
print("c1.color:  ",c1.color)
print("c1.speed:   ",c1.speed)
Car.count=10 #클래스 변수
print(Car.count)

c2=Car()
c2.color="red"
print("c2.color:  ",c2.color)#red
print("c1.color:   ",c1.color)#white
print("c2.color:   ",c2.color)#white

Car.count=200
print("c1.count: ",c1.count)
print("c2.count: ",c2.count)

c2.door=4
print("c2.door : ",c2.door)

c2.count=1 #기존 클래스변수를 지우고 인스턴스변수를 다시 생성 #100
print(c2.count) #1
print(c1.count)#200

c3=Car()
print(c3.count) #200
