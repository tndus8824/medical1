import datetime
#input 입력받은 데이터를
#AAA
#p0320.txt 파일을 생성해서 저장하시오.
#p_0320은 현재날짜를 사용하시오.

now=datetime.datetime.now()
print(now.month)
print(now.day)
print(now.strftime("%m%d"))
str1=input("글자를 입력하세요")

fileName="p_"+now.strftime("%m%d")+".txt"
with open("fileName","w",encoding="uft-8") as f:
    f.write(str1+"\n")
