in_file=None
out_file=None

in_file =open("C:/workspace/medical1/정국.jpg","rb")
out_file =open("C:/workspace/medical1/a/jjj.jpg","wb")


while True:
    bin=in_file.read(1)
    if not bin:break
    out_file.write(bin)
    
in_file.close()
out_file.close()

print("복사가 완료되었습니다.")
