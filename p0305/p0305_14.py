import operator

#딕셔너리 정렬
t_dic={}
t_list=[]
t_dic={'peach':'복숭아','orange':'오렌지','apple':'사과','pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

t_list=sorted(t_dic.items(),key=operator.itemgetter(1)) #한글순
t_list=sorted(t_dic.items(),key=operator.itemgetter(0)) #영어순

sorted(t_dic.items(),key=operator.itemgetter(0),reverse=True)

#(peach,복숭아),(orange,오렌지)...
#0번쨰 있는 방을 정렬해달라
# print(t_dic.keys())#key 값
# print(t_dic.values())#value 값
# print(t_dic.items()) #튜플



'''
#3개의 숫자를 입력받아 순서대로 출력하시오.
#17,50,12
#12,17,50
#input("{}번째 숫자를 입력하세요".format(i+1))
#
#num[i]=int(input("f{i+1}번째 숫자를 입력하세요."))
#
a=int(input("첫번째 숫자를 입력>>> "))
b=int(input("두번째 숫자를 입력>>> "))
c=int(input("세번째 숫자를 입력>>> "))
# num=[0,0,0]
# for i in range(3):
#     print(i)
#     num[i]=int(input("f{i+1}번째 숫자를 입력하세요."))
S=[a,b,c]
S.sort()
print(S)

S.sort(reverse=True)
print(S)

print("최대값 : ",max(*S))
print("최소값 : ",min(*S))
# a=[5,7,4,8,1,9,3,2]
# a.sort()
# print(a)

# b=[5,7,4,8,1,9,3,2]
# b.sort(reverse=True) #역순정렬
# print(b)
'''