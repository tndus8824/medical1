#입력 : 이름, 아이디, 비밀번호(input)
# 5명을 입력받아서 member리스트를 만드세요

member=[] #[[홍길동,aaa,1111],[유관순,bbb,1111]]

'''
member 리시트를 
이름   아이디  비밀번호

홍길동  aaaa  11111
이순신  bbbb  22222

형식으로 출력 해보세요
'''
for i in range(5):
    name=input('이름을 입력해주세요 >>>  ')
    id=input('아이디를 입력해주세요 >>>  ')
    pw=input('비밀번호를 입력해주세요 >>> ')


a=len(member)
print("이름\t아이디\t 비밀번호")
for i in range(len(member)):
    print('{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2]))