#현재까지 입력한 숫자와 결과값을 모두 출력해 보세요.

def cal(save_list):
    save_list=[0]*5
     
    for i in range(save_list[0],save_list[1]+1):
        save_list[2]+=i
        save_list[3]-=i
        save_list[4]*=i
       

#다시해보기
num1=int(input("첫번째 숫자를 입력해주세요 >>"))
num2=int(input("두번째 숫자를 입력해주세요 >>"))
#함수호출(리스트를 이용해서)
s_list=[num1,num2,0,0,0]
cal(s_list)
print("더하기 값 :",s_list[2])
print("빼기 값 :",s_list[3])
print("곱하기 값 :",s_list[4])
print(s_list)

    