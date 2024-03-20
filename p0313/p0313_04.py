#다른 파일에 있는 함수를 사용할때
# import math*->사용방법 math.floor() 이름. 함수명()
# import lotto* # 이름 생략가능
# import lotto
# from lotto import*
import math as m #모듈명을 줄여서 사용가능, 별칭부여
import lotto as lo
# l=[0]*45
# # while True:
# #     lotto.screen()
# lo.screen()
# lo.num_generate(l)

import math
#ceil - 올림
print(math.ceil(12.2)) #13
#floor- 버림
print(math.floor(12.9)) #12
#round -반올림
print(round(12.6)) #13

print(dir(m))

