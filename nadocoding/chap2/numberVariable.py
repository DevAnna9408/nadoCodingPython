# 절댓값은 abs
print(abs(-5))

# 제곱은 pow
print(pow(4, 2))

# 최대값은 max
print(max(12, 45))

#최솟값은 min
print(min(1, 2))

#반올림은 round
print(round(4.99))

# math 라이브러리를 import
from math import *

# 내림은 floor
print(floor(4.99))

# 올림은 ceil
print(ceil(4.99))

# 제곱근을 구하는 sqrt
print(sqrt(16))

# 랜덤은 random

from random import *

print(random()) # 그냥 랜덤은 0.0 ~ 1.0 사이의 값을 출력 해 준다.

# 정수만 출력하고 싶을 때는 int
print(int(random() * 10))

# 로또 번호를 출력 해 보자!
print(int(random() * 45 + 1)) # 1부터 45 이하의 임의의 값을 생성한다.

# 곱하기를 하고 싶지 않고 범위를 지정 할 때는 randrange, randint
print(randrange(1, 46)) # 대신 randrange는 미만이다.
print(randint(1, 45)) # 헷갈리니까 randint를 사용하자.

# 나도 코딩의 퀴즈

'''
월 4회 스터디르 ㄹ하는데 3번은 온라인으로 하고 1번은 온라인으로 한다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오

조건1: 랜덤으로 날짜를 뽑아야 함
조건2: 월별 날짜는 다름을 감안하여 최소 일 수 인 28 이내이다
조건3: 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외된다.
'''

print("----------")

date = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월",str(date),"일 입니다.")

print("----------")