# 리스트 [] 순서를 따지는 객체의 집합

#예: 지하철 칸 별로 10, 20, 30명이 있다고 자ㅓㅇ

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]

print(subway)

newSubway = ["김씨", "박씨", "최씨"]

# 김씨는 몇 번째인가? => index
print(newSubway.index("김씨"))

# 이씨를 추가하려면 => append
newSubway.append("이씨")
print(newSubway)

# 안씨를 김씨와 박씨 사이에 넣어보자 => insert
newSubway.insert(1, "안씨")
print(newSubway)

# 뒤에서 한 개를 뺄때는 pop
print(newSubway.pop())
print(newSubway)

# 같은 원소 갯수 찾기 => count
newSubway.append("김씨")
print(newSubway.count("김씨"))

# 정렬은 sort, 뒤집기는 reverse
numArr = [5, 2, 4, 3, 1]
numArr.sort()
print(numArr)
numArr.reverse()
print(numArr)

#모두 지울 때는 clear
# numArr.clear()
# print(numArr)

# 파이썬은 여러 자료형을 함께 사용할 수 있다.
mixList = ["숫자", 1, True]
print(mixList)

# 리스트를 확장할 때는 add가 아닌 extend
numArr.extend(mixList)
print(numArr)











