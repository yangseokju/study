""" #함수 : 반복하고 싶은 코드 덩어리를 모아 놓은 것
#비슷한 문맥에서 사용되는 함수들을 묶어서 보관(비슷한 기능을 가짐)

import random #random모듈 불러오기

# 저녁메뉴 뭐 먹지??
menu = ["치킨","마라탕","시리얼","피자","갈비"]

#이중에서 램덤으로 하나를 고르고 싶다.
dinner = random.choice(menu)
print(dinner) """

#로또번호출력 1~45 사이의 수를 6개
import random
numbers = range(1,46) #1부터 46 -1 까지의 범위
# 그 범위중에 6개를 뽑아서 리스트로 만들기
lucky_numbers = random.sample(numbers, 6)
print(sorted(lucky_numbers))