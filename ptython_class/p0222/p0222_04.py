# 두 수를 입력받아서 사칙연산을 출력해보세요
# 변수 A,B

#10+3=13
#10-3=7
#10*3=30
#10/3=3.333


A= int(input("첫번째 숫자를 입력해주세요 >>>"))
B= int(input("두번째 숫자를 입력해주세요 >>>"))
print("%d + %d =%d"% (A,B,A+B))
print("%d - %d =%d"% (A,B,A-B))
print("%d * %d =%d"% (A,B,A*B))
print("%d / %d =%.3f"% (A,B,A/B))


A= int(input("첫번째 숫자를 입력해주세요 >>>"))
B= int(input("두번째 숫자를 입력해주세요 >>>"))
print("{} + {} = {}".format(A,B,A+B))
print("{} - {} = {}".format(A,B,A-B))
print("{} * {} = {}".format(A,B,A*B))
print("{} / {} = {}".format(A,B,A/B))
