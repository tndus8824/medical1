# #stu.txt파일을 출력하세요
# file=open("str.txt","r",encoding="utf8")
# txt=file.readline()
# file.close()



# file=open("str.txt","r",encoding="utf8")
# while True:
    
#     txt=file.readline()#파일 한줄 읽어오기
#     if txt=="":
#         break
#     print(txt,end="")
    
    
    
# file.close()



#파일저장
file=open("str.txt","w",encoding="utf-8")

file.write("안녕하세요.반갑습니다.\n")
file.write("저는 홍길동입니다.\n")
file.write("파이썬 수업을 열심히 듣고 있습니다.\n")



file.close()
print("파일이 저장되었습니다.")