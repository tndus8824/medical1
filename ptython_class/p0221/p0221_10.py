#변수 3개를 만들어서 name, city, fruit
# 아래와 같이 출력해보세요
# 저의 이름은 (name) 입니다.
# 저는 (city)시에서 태어났습니다.
# 저는 (fruit)를 좋아합니다.



# print("저의 이름은 %s입니다" %name)
# print("저는 %s시에서 태어났습니다" %city)
# print("저는 %s를 좋아합니다" %fruit)

#변수선언->input으로 입력받아서 출력

# name='이름'
# city='도시'
# fruit='과일'

# name=input("이름을 입력하세요  :")
# city=input("도시를 입력하세요  :")
# fruit=input("좋아하는 과일을 입력하세요 : ")
# print("저의 이름은" +name+ "입니다") 
# print("사는곳은" +city+ "입니다")
# print("좋아하는 과일은" +fruit+ "입니다")

#숫자 하나를 입력받아서 출력해보세요 input()
#출력: 입력하신 숫자는 (1)입니다

#변수 만들어서 출력해보기
num=int(input("숫자를 입력하세요 :"))
#num=int(num)
print("입력하신 숫자는" ,num ,"입니다")
print("입력하신 숫자는 %d 입니다"%num)
print("입력하신 숫자는 {} 입니다".format(num))