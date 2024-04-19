students={"stuNo":1,"stuName":"홍길동","tel":"010-0000-0000",
          "gender":"male","id":"aaa","pw":1111}
#students["nicName"]="길동스"

print(students["stuNo"])
students["stuNo"]=students["stuNo"]+1
print(students["stuNo"])
print(students.keys())
print(students.values())
print(students.items())
for i,j in enumerate(students):
    print("{}번째 {}값".format(i,j))
    print(f'{i}번째 {j}값')
    print(list(enumerate(students)))