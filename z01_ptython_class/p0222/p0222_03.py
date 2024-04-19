#해보세요
#숫자 하나를 입력받아서 구구단(~3까지)을 출력해보세요
#숫자 하나를 입력받아서 구구단을 출력해보세요4
#출력:

#2*1=2
#2*2=4
#2*3=6

#문자열로 출력해보기

print('{}*{}={}'.format(2,1,2*1))
print('{}*{}={}'.format(2,2,2*2))
print('{}*{}={}'.format(2,3,2*3))

num =3
print('{}*{}={}'.format(num,1,num*1))
print('{}*{}={}'.format(num,2,num*2))
print('{}*{}={}'.format(num,3,num*3))

#입력을 받아서 출력
dan=int(input("구구단 몇단으로 할까요? >>>  "))

print("%d단입니다"%dan)
print('{}*{}={}'.format(dan,1,dan*1))
print('{}*{}={}'.format(dan,2,dan*2))
print('{}*{}={}'.format(dan,3,dan*3))