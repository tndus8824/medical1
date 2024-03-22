import os

#파일생성(방법1)
# f=open("students.txt","w")
# f.write(1,'홍길동',100,100,99,299,99.97,1)
# f.close() #파일닫기

#with 사용하면 f.close()사용하지 않아도 됨.
# 아니면 사용해야함.\
#파일쓰기(방법2)
t_list=[]
with open ("student.txt","w",encoding='utf-8') as f:
    f.write('1,홍길동,100,100,99,299,99.97,1\n')
    f.write('2,유관순,99,99,98,296,98.67,1')
# 파일읽기
out_f= open("student.txt","r",encoding='utf-8')
while True:
    txt=out_f.readline() #1줄씩 읽어오기
    # print(type(txt))
    print(txt)
    if txt == '':
        break
    print(txt,end="")
    t_list.append(txt)
print()
print(t_list)
out_f.close()

os.remove("student.txt")#삭제
    
#파일삭제

# print("현재 폴더내 파일들 표시 : ",os.listdir())
#폴더가 존재하는 확인
# if not os.path.exists("hello"):
#     os.mkdir("hello")
# else:
#     os.rmdir("hello")

# os.rmdir("hello")
