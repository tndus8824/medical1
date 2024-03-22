#점수를 입력받아서
#90점 이상이면 A 80점이상이면 B 70점이상이면 C 나머지는 F를 출력해보세요

#98점이상은 A+ 90-93점은 A-
#B+, B-,C+, C-(중첩 if)

S =int(input("점수를 입력해주세요 >>> "))
if S>=90:
    print("90점이상입니다")
    if S>=98:
        print("A+")
    elif S>93:
        print("A")
    else:
        print("A-")
        
    
if S>=80:
    print("80점이상입니다")
    if S>=88:
        print("B+")
    elif S>83:
        print("B")
    else:
        print("B-")
        
if S>=70:
    print("70점이상입니다")
    if S>=78:
        print("C+")
    elif S>73:
        print("C")
    else:
        print("C-")
        
else:
    print("F")   