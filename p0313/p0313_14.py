import random
c_number=[0]*13
for i in range(13):
    c_number[i]=i+1
    
c_number =[1,2,3,4,5,6,7,8,9,10,11,12,13]
s_num=random.sample(c_number,k=2)

for i in s_num:
    #i=3,5[랜덤값]
    for index, value in enumerate(c_number):
        #idex=0~12 ,value=1~13
        if i == value:
          
            print(f'{index+1}번째방', f'랜덤값:{value}')

s_num[0], s_num[1]
if s_num[0]>s_num[1]:
    print(f'{s_num[0]}이 큰수다',f'{s_num[1]}이 작은수다')
else:
     print(f'{s_num[1]}이 큰수다',f'{s_num[0]}이 작은수다')
     
