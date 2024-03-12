#조건문
#1. 키가 130cm 이상만 놀이기구를 탑승할 수 있다.
height= 120
#조건문

#2. 나이가 10살 이상이고 키가 130이상만 놀이기루를 탑승가능

age= 11

#3. 비면 [우산을 챙겨주세요] 아니면 [선크림발라주세요]출력
#4.비나 눈이면[우산을 챙겨주세요] 아니면 선크림을 발라주세요

height=120

if height>=130:
    print("탑승가능")
else:
    print("탑승불가")
b=11  
if b>=10 and height>=130:
    print("놀이기구를 탈수 있다")
else:
    print("탑승불가")

    
weather='비'
if weather =='비' :
    print("우산을 챙겨주세요")
else:
    print("선크림을 발라주세요")
    
if  weather =='비' or weather =='눈':
    print("우산을 챙겨주세요")
else:
    print("선크림을 발라주세요")
   
    