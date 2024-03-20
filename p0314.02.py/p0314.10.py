#medical_1.csv파일을 읽어와서 출력하세요

#파일열기
f=open("medical_1.csv","r",encoding="utf8")

#파일읽기
cnt = 0
sum=0
while True:
    content=f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if content =="":break
    list=content.split(",")
    list[1]=int(list[1]) #리스트 전체를 정수 변환
    sum+=list[1]
print("기초생활수급대상자 전체 수 :",sum)
#파일닫기
f.close()
        
        
        
        
        
        

        
            