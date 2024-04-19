print('2단출력')
for i in range(1,10):
    print('2*{}={}'.format(i,2*i))
for i in range(1,10):
    print('{}*{}={}'.format(2,i,2*i))
    

#원하는 단을 입력받아서 구구단을 입력하세요
#3단을 입력받으면 3단 출력

dan=int(input("몇 단 >>>  "))
for i in range(1,10):
    print('{}*{}={}'.format(dan,i,dan*i))

for i in range(5):
    dan=int(input("몇 단 >>> "))
    for k in range(1,10):
        print('{}*{}={}'.format(dan,k,dan*k))
    