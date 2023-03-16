# 문자열

sentence = '나는 사람입니다.'
print(sentence)

sentence2 = "나는 따옴표가 달라도 됩니다."
print(sentence2)

sentence3 = """
따옴표를 3개를 써도 괜찮아요.
"""
print(sentence3)

#문자열 자르기 슬라이싱

sliceStr = "940803-1234567"

print("하나만 자르기는 인덱스", sliceStr[4])
print("범위로 자르기는 콜론", sliceStr[0:3])
print("처음부터 자를때는 0 생략 가능", sliceStr[:6])
print("마지막까지 가져올 때도 마지막은 생략 가능", sliceStr[3:])
print("뒤에서부터 가져 올 때는 -", sliceStr[-7:])

# 문자열 처리 함수

pyhton = "Python is Amazing"

# 소문자로 가져 올 때는 lower
print(pyhton.lower())

# 대문자로 가져 올 때는 upper
print(pyhton.upper())

# 특정 문자가 대문자인지는 isupper()
print(pyhton[0].isupper())

# 길이를 가져 올 때는 len
print(len(pyhton))

# 문자를 변경 할 때는 replace("찾을 문자", "바꿀 문자")
print(pyhton.replace("Python", "Kotlin"))

# 위치를 찾을 떄는 index
index = pyhton.index("n")
print(index)

# 두 번째를 찾을 때는 위치? 를 넣어준다.
index = pyhton.index("n", index + 1)
print(index)

'''find를 사용해도 된다. 값이 없으면 -1을 반환 해 준다.
index로 찾을 때는 에러가 난다.
가급적이면 find를 써야겠다.
'''
print(pyhton.find("n"))

# 갯수를 찾을 때는 count
print(pyhton.count("n"))

# 문자열 포맷

# %d 뒤에 값을 할당해서 정수를 넣을 수 있다.
print("나는 %d살 입니다." %20)

# 문자를 넣을 때는 %s
print("나는 %s를 좋아합니다." % "코틀린")

# 문자가 아닌 하나의 글자는 %c
print("코틀린은 %c로 시작한다." %"K")

# %s는 만능이기 떄문에 문자 숫자 모두 사용 가능하다.

# 두 가지를 할당 할 때는 괄호 안에 넣어주면 된다.
print("인생은 %s와 %s 사이의 선택이다." % ("B", "D"))

# 중괄호를 넣어서 할 때는 .format
print("나는 {}살 입니다.".format(20))

# 물론 중괄호도 두 개가 가능하다.
print("나는 {}과 {}를 좋아한다.".format("파이썬", "코틀린"))

# 중괄호를 넣을 때는 index를 할당할 수 있다.
print("나는 {1}과 {0}를 좋아한다.".format("파이썬", "코틀린"))

# 고오급 format, 변수 할당을 할 수 도 있다.
print("나는 {age}살이고 {color}색을 좋아한다.".format(age = 20, color = "파랑"))

# f를 사용하면 정의 된 변수를 할당할 수 있다.
age = 20
color = "파랑"
print(f"나는 {age}살이고 {color}색을 좋아한다.")



