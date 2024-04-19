import operator
numbers=[1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1]
counter={}
print(counter)
counter["1"]=2
#counter["2"]=1
print(counter) # {1 : 2, 2 : 1}
for number in numbers:
    if number not in counter:# counter딕셔너리에 키값이 없으면
        counter[number]=0     #딕셔너리에 추가
                             #counter[number]=0     
    counter[number]=counter[number]+1 #딕셔너리 1을 증가
print(counter)
    
#많이 나온 숫자로 정렬(오름차순)
#print(sorted(max(),key=operator.itemgetter(0)))
#파이썬 듀타로 이해하기