# #131

# 사과
# 귤
# 수박

# #132
# for문의 핵심은 들여쓰기된 코드가자료구조에 저장된 데이터 개수만큼 반복된다.
# 세계의 데이터가 저장돼 있으므로 들여쓰기된 print(####)코드가 세번실행
# #####

# #133
# print("A")
# print("B")
# print("C")

# #134
# for문을 풀어서 동일한 동작 코드 작성

# #135
# A=["10","20","30"]
# for i in A:
#     print(i)
#138
# for i in ["10","20","30"]:
#     print(i)
#     print("-------")

#139
# print("++++")
# for i in ["10","20","30"]:
#     print(i)

#140
# for i in ['사','마',3,4]:
#   print("------")
#141
# list=[100,200,300]
# for i in list:
#   print(i+10)
# #142
# list1=["김밥","라면","튀김"]
# for i in list1:
#   print("오늘의 메뉴 : {}".format(i))
  
# #143
# list2=["sk하이닉스","삼성전자","LG전자"]
# for i in list2:
#   print(len(i))

# #144
# list3=["dog","cat","parrot"]
# for i in list3:
#   print(i,len(i))
  
# list3=["dog","cat","parrot"]
# for i in list3:
#     print(i[0])
    
  
# list4=[1,2,3]
# for i in list4:
#   print("{}x{}={}".format(3,i,3*i))

#149
# list = ["가", "나", "다", "라"]
# for i in list[::2]:
#   print(i,end="")
  
# #150  
# print()
# list = ["가", "나", "다", "라"]
# for i in list[::-1]:
#   print(i,end="")
  
#
#151
# list=[3,-20,-3,44]
# for i in list:
#   if i <0:
#     print(i)
# print()  
 
# #152
# list=[3,100,23,44]
# for i in list:
#   if i %3==0:
#     print(i)
    
#153
# list2=[13,21,12,14,30,18]
# for i in list2:
#   if i % 3==0 and i <20:
#     print(i) 

# #154
# list=["I","study","python","language","i"]
# for i in list:
#   if len(i) >=3:
#     print(i)

# #155
# list=["A","b","c","D"]
# for i in list:
#   if i == i.upper():
#     print(i)
    
# #156
# list=["A","b","c","D"]
# for i in list:
#   if i == i.lower():
#     print(i)
    
#157
# list3=["dog","cat","parrot"]

# for i in list3:
#   a1=i[0]
#   A=a1.upper() 
#   print(A+i[1:])
  
  
#158
# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# #변수 하나씩을 들고 와서 
# #그 리스트에 요소가 .으로 나뉘어진 리스트로 만든후에
# #그 리스트 자리에 "h"가 있는지 판단 있으면 출력
# for i in list:
#   split=i.split('.') #요소를 .의 기준으로 리스트로 분리시켜라!
#   if split[1]=="h":
# #     print(i)

# #159
# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in list:
#   j=i.split(".")
#   if j[1]=="h" or j[1]=="c":
#     print(i)

# #161
# for i in range(100):
#   print(i)
  
# #162
# for i in range(2002,2051,4):
#   print(i)

# #163
# for i in range(1,31):
#   if i %3==0:
#     print(i)

# #164
# for i in range(100):
#   print(99-i)

# #165
# for i in range(10):
#   print('{}.{}'.format(0,i))
  
# #166
# for i in range(1,10,1):
#   print("{}x{}={}".format(3,i,3*i))

# #167
# for i in range(1,10,2):
#   print("{}x{}={}".format(3,i,3*i))
  
# #168
# sum=0
# for i in range(10):
#   sum+=i+1
# print("합: ",sum)

# #169
# sum=0
# for i in range(1,11):
#   if i%2==1:
#     sum+=i
# print("홀수 합",sum)

# #170
# gob=1
# for i in range(1,11):
#   gob=gob*i
# print(gob)

#171
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
  print(price_list[i])
  
#172
price_list = [32100, 32150, 32000, 32500]
for i, k in enumerate(price_list):
  print(i,k)
  
#173