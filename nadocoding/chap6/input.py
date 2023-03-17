# 표준 입출력

print("자바", "코틀린", sep=",") # sep를 입력하면 각 콤마로 구분된 변수를 어떻게 출력할지 정할 수 있다.
print("자바", "코틀린", sep=",", end="?") # end를 입력하면 출력 후 원하는 행위를 할 수 있다.

# 표준 출력과 에러출력

import sys

print("성공", file=sys.stdout)
print("실패", file=sys.stderr)

# 시험 성정
scores = {"수학": 0, "영어": 50, "코딩": 100}
for sub, score in scores.items():
    print(sub.ljust(8), str(score).rjust(4), sep=":") # 정렬

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 3개만큼의 크기로 0을 넣는다.

# 입출력은 많이 사용하지 않으므로 필요할 때 나도코딩을 참고할 것