f=open("k001.csv","r",encoding="utf8")

cnt = 0
sum=0
while True:
    content=f.readline()
    if cnt == 0:
        cnt += 1
        continue
    if content =="":break
    
    new_list=content.split(",")
    new_list[3]=int(new_list[3]) #리스트 전체를 정수 변환
    sum+=new_list[3]
f.close()
print(sum)
        