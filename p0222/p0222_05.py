#국어, 영어, 수학 점수를 받아서 평균을 출력하세요
#출력:  평균은 : 95점 입니다.
#변수: kor, eng, math1

# kor=100, eng=90 , math=80

# 3가지 점수를 입력받아서 출력

kor=int(input("국어 점수를 입력하세요  >> "))
eng=int(input("영어 점수를 입력하세요  >> "))
math=int(input("수학 점수를 입력하세요  >> "))
total=kor+eng+math
avg=total/3
print("평균은 %d 입니다" % avg)


kor=int(input("국어 점수를 입력하세요  >> "))
eng=int(input("영어 점수를 입력하세요  >> "))
math=int(input("수학 점수를 입력하세요  >> "))
avg=(kor+eng+math)/3
print("평균은 %d 입니다" % avg)
print("평균은 {}점입니다".format(avg))