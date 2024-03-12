cnt=0
while True:
    print("[영단어 맞추기 프로그램]")
    print("1.명사")
    print("2.동사")
    print("3.형용사")
    print("0.종료")
    print("-"*40)

    choice =int(input("원하는 번호를 입력하세요 >> "))
    m={"airplane":"비행기",
            "apple":"사과",
            "bakery":"빵집",
            "banana":"바나나",
            "bank":"은행",
            "bean":"콩",
            "bycicle":"자전거",
            "boat":"보트",
            "bowl":"그릇",
            "bus":"버스",
            }
    d={"go":"가다",
    "come":"오다",
    "walk":"걷다",
    "sleep":"자다",
    "eat":"먹다",
    "drink":"마시다",
    "cut":"자르다",
    "run":"달리다",
    "buy":"사다",
    "plus":"더하다"}
    
    h={"accumulated":"누적된",
    "additional":"추가적인",
    "adequate":"적당한",
    "administrative":"관리의",
    "affordable":"알맞은",
    "alternative":"대체 가능한",
    "annual":"해마다의",
    "different":"다른",
    "local":"지역의",
    "social":"사회의",
    }
        
 
    if choice ==1 :
        print("1.명사를 선택하였습니다.".format())
        ch = input("퀴즈가 나갑니다.준비되셨나요? (1.실행,0.취소)")
        if ch == '1':
            #퀴즈프로그램
            #key-영어, values-한글
            # print(m.keys())- 전체 key
            # print(m.values())-전체 values
            for key in m:
                anwer=input(f'{key}단어의 뜻은?  ')
                #print(key,":",m[key])
                if m[key]== anwer:
                    cnt+=1
                    print("정답")
                else:
                    print("오답")
            print(f'정답:{cnt}개, 오답: {len(m)-cnt}입니다.')
        else:
            print("퀴즈를 취소하셨습니다.메뉴로 돌아갑니다.")

    
         
    elif choice == 2 :
        print("2.동사를 선택하였습니다.")
        ch =input("퀴즈가 나갑니다.준비되셨나요? (1.실행,0.취소)")
        if ch == '1':
            for key in d:
                an=input(f'{key}단어의 뜻은?  ')
                if d[key]== an:
                    cnt+=1
                    print("정답")
                else:
                    print("오답")
            print(f'정답:{cnt}개, 오답: {len(m)-cnt}입니다.')
            
        else:
            print("퀴즈를 취소하셨습니다.메뉴로 돌아갑니다.")
            
        
    elif ch =="3" :
        print("3.형용사를 선택하였습니다.")
        ch =input("퀴즈가 나갑니다.준비되셨나요? (1.실행,0.취소)")
        if ch == '1':
            for key in h:
                an=input(f'{key}단어의 뜻은?  ')
                if h[key]== an:
                    cnt+=1
                    print("정답")
                else:
                    print("오답")
            print(f'정답:{cnt}개, 오답: {len(h)-cnt}입니다.')
            
        else:
            print("퀴즈를 취소하셨습니다.메뉴로 돌아갑니다.")    
        pass
        print("3.형용사를 선택하였습니다.")
    elif ch =="0" :
        print("종료되었습니다")
        break

