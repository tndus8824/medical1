import operator
foods={"떡볶이":"오뎅","짜장면":"단무지","라면":"김치",
      "피자":"피클","맥주":"땅콩","삼겹살":"상추"}
f_list=[]
f_dic={}
#키의 값을 출력하시오.
#value 값을 출력하시오.
#key:value 형태로 모두 출력하시오.

print(foods.keys())
print(foods.values())
print(foods.items())

for key in foods:
      print(key,end='\t')
print()     
for key in foods:
      print(foods[key],end="\t")
print()     
for i in foods:
      print(f"{key} : {foods[key]}")
print()
print(sorted(foods.items(),key=operator.itemgetter(0)))
print(sorted(foods.items(),key=operator.itemgetter(1)))


