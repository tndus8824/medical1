#파일 1개 저장
#file open
file=open("memo.txt","w",encoding="utf8")
try :
    #file write
    file.write("안녕하세요.1\n")
    file.write("안녕하세요.2\n")
    print(1/0)
    file.write("안녕하세요.3\n")
    file.write("안녕하세요.4\n")
except Exception as e: #Exception:예외에 대한 출명을 출력
    print("저장시 에러가 났습니다.")
    print(e)
finally:
    file.close() #예외발생해도, 예외발생하지 않아도 무조건 실행

#파일닫기