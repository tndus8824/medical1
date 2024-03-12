# 해보세요
#  1.숫자 두개를 입력받아서 나누기값 몫값 나머지값을 출력
#  2. 3 개의 수의 합을 구하세요
#s1,s2,s3 ='100','100.123','99.9'
 
A=int(input("첫번째 숫자를 적어주세요 >>>"))
B=int(input("두번째 숫자를 적어주세요 >>>"))

print("두수의 나누기값은 {}입니다".format(A/B))
print("두수의 몫은 {}입니다".format(A//B))
print("두수의 나머지은 {}입니다".format(A%B))

print("나누기값: {} \n몫:  {} \n나머지:  {}".format(A/B,A//B,A%B))

s1,s2,s3 ='100','100.123','99.9'
s1=int(s1)
s2=float(s2)
s3=float(s3)

result= int(s1)+float(s2)+float(s3)
result=s1+s2+s3
print(result)