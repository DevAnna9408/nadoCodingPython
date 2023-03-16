# 파이썬의 딕셔너리

# key와 value로 구성되어있고 key중복이 허용되지 않는다.

cabinet = {3:"김씨", 100:"이씨"}
print(cabinet[3]) # key값을 넣어주면 value가 프린트 된다.
print(cabinet[100]) # 배열이랑 헷갈리지 말자

print(cabinet.get(3)) # get으로 꺼내올 수 도 있다.

# 대괄호로 값을 가져 올 때 값이 없으면 error, get으로 가져오면 none으로 가져오게 된다.

# print(cabinet[5])
print(cabinet.get(5))

# 값을 먼저 확인하고 싶으면 key in dictionary
print(5 in cabinet)
print(3 in cabinet)

# 딕셔너리를 추가하고 싶을 때는 대괄호로 할당하면 된다.
cabinet[5] = "박씨"
print(cabinet)

# 변경하고 싶을 때는 직접 할당하면 된다.
cabinet[5] = "구씨"
print(cabinet)

# 값을 지울 때는 del
del cabinet[5]
print(cabinet)

# key들만 출력하고 싶을 때는 keys(), 값만 출력하고 싶을 때는 values(), 모두 출력 할 때는 items
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 값을 모두 지울 때는 clear()
cabinet.clear()
print(cabinet)