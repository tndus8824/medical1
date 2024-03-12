import random
'''
cnt=0
l_input=input("복권을 입력하세요.(예:1조111)")
lotto='1조111'
for i in range(len(lotto)):    
    if lotto[i]==l_input[i]:
        cnt+=1

print("맞는개수 :",cnt-1) #'조'는 제외
'''
cnt=0
#1개만 맞춤
f_num=random.randint(1,9)
last_num=random.randint(0,999999)
#lotto="1조740042"
lotto=str(f_num)+"조"+"{:06d}".format(last_num)
print(lotto)

l_input=input("복권을 입력하세요.(예:1조740042)")
for i in range(len(lotto)):    
    if lotto[i]==l_input[i]:
        cnt+=1
print("맞는개수 :",cnt-1) 

#맞는개수 찾기
l_input=input("복권을 입력하세요.(예:1조740042)")
for i in range(len(lotto)):    
    if lotto[i]==l_input[i]:
        cnt+=1 
print("맞는개수: ",cnt-1)
#6번쨰 자리를 맞추면 1만원


