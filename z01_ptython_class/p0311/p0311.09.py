def plus (v1,v2):
    v1=v1+100 #101
    v2=v2+200 #202
    return v1+v2
#함수호출
v1=1
v2=2
v1,v2=plus(v1,v2) #변수값을 담아야 출력이 가능
#출력
print(v1,v2)