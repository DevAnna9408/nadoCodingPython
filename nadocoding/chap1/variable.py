# 변수

# 파이썬은 바로 선언하고 할당하면 된다.
animal = "강아지"
name = "보리"
age = 12
hobby = "산책"
isAdult = age > 3

print("우리집 " + animal + "의 이름은 " + name + "입니다.")

# 정수형을 문자로 print 하기 위해서는 str을 붙여줘야 한다.
print(name + "(은)는" + str(age) + "살이고" + hobby +"을 좋아합니다.")

'''
Boolean도 str을 붙여줘야 print가 가능하고 문자를 붙일 때 + 가 아니라 , 로도 표현이 가능하다.
콤마는 띄어쓰기를 포함한다.
'''

print("연탄이는 어른일까요?",str(isAdult))

# 나도코딩의 문제
# 변수를 이용해 다음 문장을 출력하시오

'''
변수명 station
변수값: 사당, 신도림, 인천공항을 순서대로 입력
출력 문장: 00행 형차가 들어오고 있습니다.
'''

fromStation = "사당"
toStation = "신도림"
station = "인천공항"

print(fromStation,"에서",toStation,"로 가는 열차가",station,"에 도착하고 있습니다.")


