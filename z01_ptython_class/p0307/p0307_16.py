list=[1,2,3]
alist=list #공간같이 쓴다. #얕은복사
alist=[*list] #1.깊은복사
alist=list[:] #2.깊은복사
alist=[]
list[0]=100
print(alist)

a=100
b=a
a=10
print(b)

#듀터로 돌려 보기