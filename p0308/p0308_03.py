#[
#  [0],[0],[0]...... 52개를 생성하세요
#]

#2차원 리스트 빈공간만들기

#aa=[[0]*1]*52 #얕은 복사이기에 쓸수 없음
bb=[[0]*2 for i in range(52)]
cc=[]
for i in range(52):
    dd=[]
    for i in range(2):
        dd.append(0)
    cc.append(dd)
print(cc)


#1차원 리스트 빈공간 만들기
# a_list=[0]*52
# b_list=[]
# for i in range(52):
#     b_list.append(0)
# c_list=[i for i in range(52)]


#b_list=[]
#for i in range(52):
#    b_list.append(i)

