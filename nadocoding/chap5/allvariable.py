# 가변인자

def profile(name, age, *lang): # 와일드카드를 넣으면 얼마든지 가변으로 인자를 받을 수 있다.
    print("이름은 : {0}\t나이: {1}".format(name, age), end = " ") # end를 사용하면 줄바꿈을 하지 않고 띄어쓰기만 하라는 뜻
    # print(lang) #end가 있기 때문에 두 문장이 하나의 문장으로 출력된다.
    for l in lang:
        print(l, end=" ")
    print()

profile("김씨", 20, "파이썬", "코틀린")
profile("김씨", 20, "자바")

# 전역변수와 지역변수

gun = 10

def checkPoint(sol):
    global gun # 전역 공간에 있는 변수를 사용하는 global, 파이썬은 지역변수를 선호한다.
    gun = gun - sol
    print("함수 내 남은 총 : {0}".format(gun))

def checkPointReturn(gun, sol):
    gun = gun - sol
    print("함수 내 남은 총 : {0}".format(gun))
    return gun

gun = checkPointReturn(gun, 2)
print(gun)

# checkPoint(2)

# 나도코당의 문제

'''
표준 체중을 구하는 프로그램을 작성하시오

표준 체중: 각 개인의 키에 적당한 체중

남자: 키 * 키 * 22
여자: 키 * 키 * 21

조건1: 표준 체중은 별도의 함수 내에서 계산
함수명: std_weight
전달값: 키, 성별

조건2: 표준 체중은 소수점 둘째자리까지 표시

출력 예제: 키 000 남자의 표준 체중은 00kg 입니다.

'''

def std_weight(height, gender):
    if gender == "men":
        return round(height * height * 22, 2) # round 뒤에 콤마 숫자를 입력하면 소수점 자리수를 출력할 수 있다.
    else:
        return round(height * height * 21, 2)

gender = input("성별은? : ")
height = int(input("키는? : "))

print(std_weight(height / 100, gender))