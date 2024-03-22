def func(n,*val,a=2): #기본매개변수,가변매개변수,키워드변수 순서로 들어와야함.
    for i in range(n):
        for v in val:
            print(v)
            
func(5,"안녕","안녕하세요.","반갑습니다","매개변수")















# print(range(10))
# a=range(10)
# print(a)
# print(list(range(10)))


# print([i for i in range(10)])

