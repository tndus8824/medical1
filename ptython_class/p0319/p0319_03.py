class Student:
    count = 1 # 클래스 변수 사용
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count  # 클래스변수 사용
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total/3))
        if rank != 0:
            self.rank = rank
    def __str__(self): #객체를 호출하면 출력됨.
        return f"학생성적 : {self.stuNo},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
# 파일 불러와서 저장하기
students = []
f = open("stu.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "": break
    txt_list = txt.split(",")
    # 1,홍길동,99,99,87,285,95.0,1
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
# 리스트 출력
for stu in students:
    print(stu)
    
    
# 1,'홍길동',100,99,87,286,95.33,2
# 2,'유관순',98,93,87,278,92.67,3
# 3,'이순신',88,76,30,194,64.67,5
# 4,'김구',100,100,100,300,100.00,1
# 5,'강감찬',98,85,44,227,75.67,4
   

    
    
    

