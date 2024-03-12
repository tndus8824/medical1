# 동전 교환 프로그램
# 100원 동전개수
# 50원 동전개수
# 10원 동전개수


money= int(input("교환할 돈을 입력 하세요 >>>"))
c500=money//500
c100=(money%500)//100
c50=(money%100)//50
c10=(money%50)//10
c1=(money%10)
print("입력한 금액 :{}원".format(money))
print("500원 : {}개".format(c500))
print("100원 : {}개".format(c100))
print("50원 : {}개".format(c50))
print("10원 : {}개".format(c10))
print("잔돈: {}원".format(c1))