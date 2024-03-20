#1.파일열기
f=open('str.txt','r',encoding='utf-8')

#read():모든 문자열을 가져옴
#readline() :1줄씩 가져옴
#readlines():1줄씩 리스트타입에 입력해서 모두 가져옴

#3.파일닫기
f.close() 
    

#4.파일확인
import os
if os.path.exists("str.txt"): #파일존재 확인
    # f=open('str.txt','r',encoding='utf-8')
    with open('str.txt','r',encoding='utf-8')as f: # 변수명을 뒤에 씀
        txt_list=f.readlines()
    for txt in txt_list:
        print(txt,end="")
        print()
        #with쓰면 close안해도 됨.
#     print(txt_list)
# txt=f.readlines()
# print(txt)
# print(txt[0])
# f.close()