#구구단 -이중for문을 사용하고 있음.
#변수 1개 사용
temp=0
for i in range(1,10):
    if i ==2: 
        break
    for j in range(2,10):
        if j ==5:
                break
        print(f'{i}*{j}={i*j}',end='\t')
    if temp ==1: break
print()
    
   
for i in range(1,10):
    if i ==2: 
        break
    for j in range(2,10):
        if j ==5:
                break
        print(f'{i}*{j}={i*j}',end='\t')
  
