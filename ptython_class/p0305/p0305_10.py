a=[1,2,3,4]
b = a #얕은 복사
c=[*a] #전개여난ㅅ자
#a의 데이터 값을 변경
a[1] = 20
print(b)#변경이 됨
print(c)#변경이 안됨
#c=[a]  변경이 안됨
#다시
product=["새우깡","90g",1200,3]
print("상품 : {},무게 : {},가격: {},유통기한 :{}").format((product[0],product[1],product[2],product[3]))
print(("상품 : {},무게 : {},가격: {},유통기한 :{}").format(*product))


