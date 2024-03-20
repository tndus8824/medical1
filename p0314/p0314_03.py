#외부와의 데이터 전송,외부기기 연결,다른 프로그램 연결
#이런 곳 외에는 되도록 여러분이 프로그램이 오류 발생되지 않도록
#하는게 가장 좋음
print("프로그램 실행")
try:
    print(1)
    print(2)
    # print(1/0) #에러가 발생
    print(3)
except:#예외가 발생하면 실행
    print(4)
    print(5)
else: #예외가 발생하지 않으면 실행
    print(6)
finally:#예외가 발생하거나, 하지 않거나 무조건 실행
    print(7)
    

print("프로그램 종료")

