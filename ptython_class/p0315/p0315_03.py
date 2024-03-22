import p0315_02

member=p0315_02.idpw()
print(member)

#mem.txt 파일에 
# aaa,1111 저장하시오

    
f=open("mem.txt","w",encoding="utf-8")

for m in member:
    f.write("{}.{}\n".format(m[0],m[1]))
    
# f.write("aaa,1111/n")
# f.write("bbb,222/n")
# f.write("ccc,222/n")
f.close()
print("파일이 저장되었습니다.")
