#stu.txt파일을 출력하세요
file=open("stu.txt","r",encoding="utf-8")
print("[학생성적입력]")
print("-"*40)
while True:
    txt=file.readline()
    text_list=txt.split(",")
    print(text_list) 
 
    stuNo,name,kor,eng,math,total,avg=text_list
        
    for i in text_list:
        print(i,end='\t') 
    text_list[0]=int(text_list[0].strip())
    text_list[1]=text_list[1].strip()
    text_list[2]=int(text_list[2].strip())
    text_list[3]=int(text_list[3].strip())
    text_list[4]=int(text_list[4].strip())
    text_list[5]=int(text_list[5].strip())
    text_list[6]=float(text_list[6].strip())
    print(text_list)
    for i in range(len(text_list)):
        print(type(text_list[i]))
  
    break
file.close()
