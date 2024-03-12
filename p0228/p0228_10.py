#중첩 for
#for 안에 for
for i in range(3):
    print('i= ',i)
    for j in range(2):
        print('j= ',i)
#i = 0 일때
   #j = 0, j = 1
#i = 1 일때
   #j= 0, j=1
#i = 2 일때
    #j=0,  j=1












#for 문을 사용해서 2단을 출력
'''
for i in range(1,10):
    print('{}*{}={}'.format(2,i,2*i))
#입력받은 숫자의 단을 출력하세요

# 3을 입력받으면 3단 출력, 4를 입력 받으면 4단 출력
'''
'''
dan=int(input("몇 단으로 할까요?  >>> "))
for i in range(1,10):
    print('{}*{}={}'.format(dan,i,dan*i))
''' 
'''
dan=int(input("몇 단으로 할까요?  >>> "))
for i in range(1,10):
    print('{}*{}={}'.format(dan,i,dan*i))
'''
for i in range(2,10):
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j))
'''        
#출력형태
# 1 2 3 4 5 
for j in range(5): #j=0,1,2,3,4
    print(j+1,'번째출력')
    for i in range(1,6):# i=1,2,3,4,5
        print(i,end=' ')
    print()
print('for 끝')
'''
'''
#전체 구구단
for i in range(2,10):
    print('[{}단]'.format(i))
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()
'''
#짝수단만 출력해주세요
for i in range(2,10):
    if i %2==0:
        print('[{}단]'.format(i))
        for j in range(2,10,2):
            print('{}*{}={}'.format(i,j,i*j),end=' ')
        print()
#홀수다만 출력해주세요   
for i in range(2,10):
    if i %2==1:
        print('[{}단]'.format(i))
        for j in range(2,10,2):
            print('{}*{}={}'.format(i,j,i*j),end=' ')
        print()
    
#(*1,3,5,7,9)출력 #
for i in range(2,10):
    if i %2==1:
        print('[{}단]'.format(i))
        for j in range(2,10,2):
            if j%2==1:
                print('{}*{}={}'.format(i,j,i*j),end=' ')
        print()