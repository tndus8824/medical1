stu=[
    ["홍길동",100],
    ["유관순",98],
    ["이순신",95],
    ["김구",50],
    ["강감찬",99],
    ["김유신",90],
    ["홍길순",80],
    ["홍길자",70],
]

#이름으로 검색해서 홍이 들어 가는 사람을 모두 검색해서 출력하시오.
#이름으로 검색해서 신이 들어 가는 사람을 모두 검색해서 출력하시오.

while True:
    search=input("이름을 검색해주세요")
    search_list=[]
    cnt=0
    for i in stu:
        for j in i:
            if j.find(search)!=-1:#-1은 찾았는데 없냐? 없으면 저장시키지마
                    search_list.append(cnt)
            cnt+=1
            if len(search_list) == 0:
                print("찾는 사람이 없습니다.")
            else:
                print(f'{search}으로 검색된 사람: ')
                for i in search_list:
                    print(stu[i][0])
                print()
                print()
        
        
            
                  
      
