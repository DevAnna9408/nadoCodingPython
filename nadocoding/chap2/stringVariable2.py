# 문자열 두 번째

# 탈출문자1 \n
print("줄바꿈은 \n 이렇게")

# 탈출문자 2 \를 따옴표 앞에 붙여준다.
print("탈출문자는 \"이렇게\" 사용한다.")

# 역슬래시를 두 번 사용하면 하나의 역슬래시로 변경된다.
print("탈출문자는 \\이렇게\\ 사용한다.")

# 커서를 맨 앞으로 이동하려면 \r
print("Red Apple\rPine")

# 문자를 삭제하려면 \b
print("Redd\bApple")

# 키보드에서 탭을 치려면 \t
print("Red\tApple")

# 나도 코딩의 문제

'''
사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예: http://naver.com

규칙1: http:// 부분을 제외 => naver.com
규칙2: 처음 만나는 점 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 e갯수 + !로 구성 => nav51!
'''

url = "http://naver.com"

newStr = url.replace("http://", "") # 규칙1
newStr = newStr[:newStr.index(".")] # 규칙2
password = newStr[:3] + str(len(newStr)) + str(newStr.count("e")) + "!"
print("{}의 비밀번호는 {}입니다.".format(url, password))

