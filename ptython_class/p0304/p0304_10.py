a= 10
b= a
b=100
print(a) #값? 10
print(b) #값? 100
a_list=[1,2,3]
b_list=a_list #값이 하나일때 주소값을 복사하기 때문에 같은주소로 바라본다.
b_list[0]=200
print(a_list[0])#1->200이 된다.(같은주소)
print(b_list[0])#200

print(a)
print(b)
print(a_list)