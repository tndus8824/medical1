
'''
#빈 리스트로 생성
cont=[]

c1= input("1.나라를 입력해주세요 >>")
c2= input("2.나라를 입력해주세요 >>")
c3= input("3.나라를 입력해주세요 >>")
c4= input("4.나라를 입력해주세요 >>")

cont=[c1,c2,c3,c4]
print('방법1',cont)

#cont.append(변수)
contA=[]
contA.append(c1)
contA.append(c3)
contA.append(c2)
contA.append(c4)
print('방법2',contA)



#미국-영국-프랑스- 이탈리아
print('{}{}{}{}'.format(c1,c2,c3,4))
#cont=[c1,c2,c3,c4]
#contA=[]<=append로 채움
print('{}-{}-{}-{}'.format(cont[0],cont[1],cont[2],cont[3]))
'''
f=[] #과일리스트
#내가 입력한 과일들로 리스트를 채워보세요

f=[]
a1=input("과일을 입력하세요  >>")
a2=input("과일을 입력하세요  >>")
a3=input("과일을 입력하세요  >>")
a4=input("과일을 입력하세요  >>")
f=[a1,a2,a3,a4]
print(f)


f=[]
f.append(a1)
f.append(a2)
f.append(a3)
f.append(a4)
print('내가 좋아하는 과일은 {},{},{},{}입니다'.format(f[0],f[1],f[2],f[3]))