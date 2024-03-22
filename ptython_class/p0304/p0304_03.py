#이름,국어,영어,수학을 입력받아
#합계를 출력하시오
students=[]
st=[]
for i in range(0,3): #for문
    student=[] #초기화
    student.append(input('이름을 입력해주세요 >>> '))
    student.append(int(input('국어점수를 입력해주세요 >>> ')))
    #kor=int(input('국어점수를 입력하세요 >>> ))
    student.append(int(input('영어점수를 입력해주세요 >>> ')))
    student.append(int(input('수학점수를 입력해주세요 >>> ')))
    sum=student[1]+student[2]+student[3]
    student.append(sum)
    student.append('{:.2f}'.format(sum/3))
    students.append(student)
    print(student)
    print(students)

    print("[학생성적 출력]")
    print("-"*40)
    print("이름\t국어\t영어\t수학\t합계\t평균\n")
        
#2차원 리스트는 for 문을 2번 사용함.
#전체출력
    for stu in students:
        for s in stu:
            print(s,end='\t')
        print()
    print()
print("-"*50) 
  
#3명의 국어점수 총합계,총합계평균을 출력하세요.
#총학생의 총국어점수, 영어점수,수학점수,합계,평균
kors=0
engs=0
maths=0
totals=0
avgs=0
#2차원리스트에서>1차원리스트,index순서를 나타낼때
for i,stu in enumerate (students):
    kors=kors+stu[1] #리스트의 [1]순서인 국어점수만 더하세요.
    engs=engs+stu[2]
    maths=maths+stu[3]
    totals=totals+stu[4]
avgs= totals/len(students)
print(' ',kors,engs,maths,totals,avgs,sep='\t')
    
print("3명의 국어 점수의 총합은 {}".format(kors))
print("3명의 총합계 평균은 {}".format(avgs))
    

