import random
words = [{},
    { "airplane":"비행기","apple":"사과","bakery":"빵집",
      "banana":"바나나","bank":"은행","bean":"콩",
      "bicycle":"자전거","boat":"보트","bowl":"그릇","bus":"버스"},
    { "run" : "달리다","walk" : "걷다","sit" : "앉다",
      "stand" : "서다","sleep" : "자다","read" : "읽다",
      "look" : "보다","do" : "하다","feel" : "느끼다","go" : "가다"},
    { "accumulated":"누적된","additional":"추가적인","adequate":"적당한",
    "administrative":"관리의","affordable":"알맞은","alternative":"대체 가능한",
    "annual":"해마다의","different":"다른","local":"지역의","social":"사회의"}
]

choice =1
print(words[choice].keys())
#dict_keys(['airplane', 'apple', 'bakery', 'banana', 'bank', 'bean', 'bicycle', 'boat', 'bowl', 'bus'])
w_list=list(words[choice].keys())
#['airplane', 'apple', 'bakery', 'banana', 'bank', 'bean', 'bicycle', 'boat', 'bowl', 'bus']
print(w_list)
new_list=random.sample(list(words[choice].keys()),5)
#['bus', 'bicycle', 'bean', 'bowl', 'boat']
print(new_list)

print()
choice =2
print(words[choice].keys())
#dict_keys(['airplane', 'apple', 'bakery', 'banana', 'bank', 'bean', 'bicycle', 'boat', 'bowl', 'bus'])
w_list=list(words[choice].keys())
#['airplane', 'apple', 'bakery', 'banana', 'bank', 'bean', 'bicycle', 'boat', 'bowl', 'bus']
print(w_list)
new_list=random.sample(list(words[choice].keys()),5)
#['bus', 'bicycle', 'bean', 'bowl', 'boat']
print(new_list)

