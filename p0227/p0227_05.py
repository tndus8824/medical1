
#0- 20 사이의 5의 배수로 이루어진 리스트를 만들어 보세요
num=[]
num1=[]
for i in range(0,21,5):
    num.append(i)
    #i=0 일때 [0]
    #i=1 일때 [0,]
    
print(num)

for i in range(21):
    if i % 5 == 0:
        num1.append(i)        
print(num1)
    

lan=['c','python','java','jquery','css']

#1.하나하나 출력해보기
#2.카운터변수 i 사용해서.
# 1.c
# 2.python
# 3.java
# 4.jquery
# 5.css

for i in lan:
    print(i)

#for i in range(1,6,1):
    #print('{}. {}'.format(i,lan[i-1]))   
    
    
for i in range(len(lan)):
    print(str(i+1)+'.',lan[i])
    #print('{}. {}'.format(i+1,lan[i]))
    
    
num=[1,-1,2,3,-4,5,6,-8,9,-10]

#양수면 양수 음수면 음수 출력 for 사용
#1:양수
#-1:음수
#2: 양수


for i in num:
    if i>=0:
        print('{}: 양수'.format(i))
    else:
        print('{}: 양수'.format(i))
        
for i in range(len(num)): 
    if num[i]>=0:
        print('{}: 양수'.format(num[i]))
    else:
        print('{}: 음수'.format(num[i]))
        
