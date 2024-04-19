students = [] 
while 1:
    process_status = False
    print('-'*20)
    print('[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생검색')
    print('5. 학생성적출력')
    print('6. 등수처리')
    print('7. 학생정렬')
    print('0. 프로그램종료')
    print('-'*20)
    stu_num = 5 
    menu_num = input('원하는 메뉴 번호를 선택하세요. >>')
    if not menu_num.isdigit() or not (0 <= int(menu_num) < 8): # 입력이 숫자가 아닌경우와 메뉴에 없는 숫자 번호일 경우
        print('입력이 잘못되었습니다. 다시 선택해주세요.')
    else:
        # 학생성적입력
        if menu_num == '1':
            print('학생성적을 입력합니다.')
            while not process_status:
                student = {} # 학생 하나의 정보
                student['학번'] =  f'K{stu_num:03d}'
                stu_name = input('학생 이름을 입력해주세요. >>')
                student['이름'] = stu_name
                stu_kor = int(input('국어 점수를 입력해 주세요. >>'))
                student['국어'] = stu_kor
                stu_eng = int(input('영어 점수를 입력해 주세요. >>'))
                student['영어'] = stu_eng
                stu_math = int(input('수학 점수를 입력해 주세요. >>'))
                student['수학'] = stu_math
                stu_sci = int(input('과학 점수를 입력해 주세요. >>'))
                student['과학'] = stu_sci
                stu_total = stu_kor + stu_eng + stu_math + stu_sci
                student['총점'] = stu_total
                stu_avg = round(stu_total / 4, 2)
                student['평균'] = stu_avg
                if len(student) != 8:
                    print('정보가 누락되었습니다. 다시 입력해주세요')
                    continue
                else:
                    print('성적 입력이 완료되었습니다.')
                    students.append(student)
                    stu_num += 1
                    process_status = True