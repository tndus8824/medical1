#리스트 
#대괄호로 감싸서 나타내며 0개 이상의 원소가 저장될 수 있습니다
num =1
num =2
print(num)

listA=[1,2]
listB=[]

n1=1
n2=2
n3=3
n4=4
n5=5

list1=[1,2,3,4,5]
list2=['사과','복숭아','딸기','배','수박']
#python의 경우 여러형태의 변수를 섞어서 사용할 수 있다
list3=[1,'홍길동',99.1] #정수 #문자 #실수

print(list2)
print(list2[1])

#list 에 4를 출력
print(list[3])
#list 에 99.1을 출력
print(list[2])
#대괄호에 음수를 넣으면 뒤 요소부터 출력이된다.
print(list[-1]) #리스트의 마지막요소는 -1로 표현할 수 있다.

#리스트의 길이 출력
a=len(list2)
print(a)
print(len(list2))

#딸기를 출력해보세요
list2=['사과','복숭아','딸기','배','수박']
print(list2[2])
print(list2[-3])

print(list[len(list2)-2])
#리스트 슬라이싱
aa=[0,1,2,3,4,5,6,7,8,9,10]
print(aa)
print(aa[1:4]) #1이상 4미만 :[1,2,3]
print(aa[3:8]) #3이상 8미만 :[3,4,5,6,7]
print(aa[2:]) #2번부터 끝까지
print(aa[:7]) #처음부터 7미만까지
print(aa[:]) #처음부터 끝까지
print(aa[1:-1]) #1이상 끝 바로 앞까지[1,2,3,4,5,6,7,8,9,10]

#요소확인: 내부에 포함되어 이는지 확인하는 방법을 제공해줌
#in, not in
print('포도'in list2)
print(11 in aa)
print(0 not in aa)

listC=[1,2,3,['a','b','c'],[4,5]]
#      0 1 2      3          4
print(list[0])
print(list[3])
print(list[4])
print(1 in listC) #true
print(4 in listC) #Flase
print([4,5]in listC) #True

