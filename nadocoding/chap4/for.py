# 반복문

for num in list(range(1, 20)):
    print("번호는 다음과 같습니다.: {}".format(num))

for cnt in range(10):
    print("이것은 점점 커지는 숫자입니다 : {}".format(cnt))

customer = "김씨"
index = 5
while index >= 1:
    print("{0} {1}번 불렀습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("5번 불렀습니다.")

# person = "Unknown"
#
# while person != customer:
#     print("{0}은 누구인가요?".format(customer))
#     person = input("이름을 입력하세요")

# 출석번호 1, 2, 3, 4, 5 앞에 100을 붙이기로 했다고 가정
students = range(1, 6)
students = [i + 100 for i in students] # 번호를 하나씩 뽑는데, i 에 100을 더한 값을 배열에 새롭게 추가
print(students)

stuLen = ["한", "글자", "두글자"]
stuLen = [len(i) for i in stuLen]
print(stuLen)

upper = ["helle", "world"]
upper = [i.upper() for i in upper]
print(upper)

# 나도 코딩의 문제

'''
당신은 카카오 택시를 이용합니다.
50명의 승객과 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

조건1: 승객별 운행 소요 시간은 5 - 50분 사이의 난수이다.
조건2: 당신은 소요시간 5 - 15분 사이의 승객만 매칭한다.

출력 예제:

1번째 손님 (소요시간: 15분)
2번째 손님 (소요시간: 15분)
...
50번째 손님 (소요시간: 15분)
'''

from random import *

customer = range(1, 51)
time = range(5, 51)
cnt = 0

for i in customer:
    realTime = sample(time, 1)[0]
    if realTime > 15:
        continue
    else:
        cnt += 1
        print("{0}번째 손님. 소요시간 {1}분".format(i, realTime))

print("총 탑승 승객 수는 {0}명 입니다.".format(cnt))

# while 추가
absent = [2, 5]
noBook = [7]
for stu in range(1, 11):
    if stu in absent:
        continue
    elif stu in noBook:
        break
    print("{0}, 책을 읽어봐".format(stu))


