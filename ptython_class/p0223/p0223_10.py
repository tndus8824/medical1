#해보세요
#성별, 키를 입력받아서
#남자일 경우(m) 172.5이상이면 [평균이상] 이하면 [평균이하]
#여자일 경우(f) 159.6이상이면 [평균이상] 이하면 [평균이하]
#그외는 잘못입력하셨습니다
#라고 추력해보세요

gender =input('성별을 입력하세요  : (mM/fF) >>')
if gender == 'm' or gender == 'f':
    pass
else:
    print("성별 입력이 잘못되었습니다.")
height= float(input('키를 입력하세요 >>'))

if gender == 'm'or gender == 'M':
    print('남성')
    if height >=172.5:
        print('평균이상')
    else:
        print("평균이하")
elif gender == 'f'or gender == 'F':
    print('여성')
    if height >=159.6:
        print('평균이상')
    else:
        print("평균이하")
    
else: 
    print("잘못입력하였습니다")
#다시하기
             