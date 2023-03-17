# 자료구조의 변경

# menu는 중괄호로 선언되었기 때문에 set
menu = {"커피", "우유", "주스"}
print(menu)

# 배열로 바꾸고 싶을 때는 list
menu = list(menu)
print(menu)

# 튜플로 바꾸고 싶을 때는 tuple
menu = tuple(menu)
print(menu)

# 당연히 세트로 바꾸고 싶을 떄는 set
menu = set(menu)
print(menu)

# 나도 코딩의 문제

'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1 - 20이라고 가정
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle과 sample을 활용한다.
'''

# 예시
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst) # 값을 섞어준다.
# print(lst)
# print(sample(lst, 2)) # 배열에서 n개를 무작위로 뽑아준다.

from random import *

# 조건1, 20명의 참가자
arr = list(range(1, 21)) # range를 사용하면 배열을 쉽게 만들 수 있다.

# 조건2, 배열을 섞은 후 4명을 추출
shuffle(arr)
coupon = sample(arr, 4)
print(coupon)

# 조건3, 치킨1명 커피 3명

print("치킨 당첨자: {}".format(coupon[0]))
print("커피 당첨자: {}".format(coupon[1:4]))


