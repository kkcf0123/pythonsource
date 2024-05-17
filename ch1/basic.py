# # 모듈
# # 함수, 변수, 클래스를 모아 놓은 파이썬 파일

# # 파이썬에서 제공하는 기본 모듈

# import math

# print(math.ceil(3.14))
# print(math.sin(1))
# print(math.cos(1))
# print(math.floor(3.14))

# print()

# import random

# print(random.random())  # 0 <= x < 1.0
# print(random.randrange(1, 10))  # 1 ~ 10
# print(random.randrange(10))  # 0 ~ 10
# print(random.choice([1, 2, 3, 4, 5, 6]))  # 리스트 내부의 요소 중 임의 선택
# print(random.shuffle([1, 2, 3, 4, 5, 6]))  # 섞기
# print(random.sample([1, 2, 3, 4, 5, 6], k=2))  # 리스트 내부 요소 중 k 개 추출

# print()

# import time

# print("지금부터 5초 정지")
# time.sleep(5)
# print("프로그램 종료")

# print()

# import datetime

# datetime 모듈 안의 datetime 클래스 now 메소드
# now = datetime.datetime.now()
# print(now)
# print(
#     f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초"
# )

# 모듈 import
# import 모듈명
# from 모듈명 import 사용할 것만 나열
# import 모듈명 as 별칭
# from math import sin, cos, floor, ceil

# print(ceil(3.14))
# print(sin(1))
# print(cos(1))
# print(floor(3.14))

import math as m

print(m.ceil(3.14))
print(m.sin(1))
print(m.cos(1))
print(m.floor(3.14))
