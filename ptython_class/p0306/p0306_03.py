import operator

#numbers에 있는 숫자들이 몇번 나왔는지
#딕셔너리로 정리출력하시오
numbers=[1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1]

counter={}

for i in numbers:
    if i not in counter:
        counter[i]=0
    counter[i]+=1
    
print(counter)
print(sorted(counter.items(),key=operator.itemgetter(0)))

array=["F","D","A","C","A","C","F","B","C","E"]

counter1={}

for j in array:
    if j not in counter1:
        counter1[j]=0
    counter1[j]+=1
print(counter1)

print(sorted(counter1.items(),key=operator.itemgetter(1)))
print(sorted(counter1.items(),key=operator.itemgetter(0)))