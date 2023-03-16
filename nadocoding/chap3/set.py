# 세트는 집합이라는 뜻으로 중복이 되지 않고 순서가 없는 배열이다.

# 세트는 중괄호로 표현한다.
mySet = {1, 2, 3, 3, 3}
print(mySet)

java = {"김", "나", "박", "이"}
python = set(["김", "나"])
print(python)

# 두 가지의 교집합은 & 혹은 intersection를 사용
print(java & python)
print(java.intersection(python))

# 두 가지의 합집합은 | 혹은 union
print(java | python)
print(java.union(python))

# 대신 세트는 순서가 없기 때문에 출력은 아무렇게나 된다..

#차집합은 - 혹은 difference
print(java - python)
print(java.difference(python))

# 값을 추가 할 때는 add
python.add("박")

print(python)

# 역시 순서가 없기 때문에 마음대로 들어간다.

# 값을 삭제 할 때는 remove
python.remove("박")
print(python)