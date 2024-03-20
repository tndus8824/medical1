import os
print("현재 운영체제 : ",os.name)
print("현재 폴더위치 : ",os.getcwd())
print("현재 폴더내 파일들 표시 : ",os.listdir())

# #폴더 생성
#os.mkdir("hello")

# #폴더 삭제
# os.rmdir("hello")

# #파일생성
# with open ("student.txt","w") as f:
#     f.write(1,'홍길동',100,100,99,299,99.97,1)

#중요!합니다~~ 
str="1,'홍길동',100,100,99,299,99.97,1"
s_list=str.split(",")
print(s_list)

for i in s_list:
    print(i,end=' ')

str='신,수,연'
print(str.split(","))

