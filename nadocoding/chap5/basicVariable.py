# 기본값

def profile(name, age, mainLang):
    print("이름 {0}\t나이:{1}\t주 사용언어: {2}" \
          .format(name, age, mainLang)) # 역슬래시 엔터를 치면 줄바꿈이 된다.


profile("안씨", 20, "코틀린")
profile("김씨", 20, "자바")

#같은 학교, 학년, 반, 수업을 받는다고 가정 할 경우 기본값을 사용

def profile_basic(name, age = 17, mainLang = "파이썬"):
    print("이름 {0}\t나이:{1}\t주 사용언어: {2}" \
          .format(name, age, mainLang))

profile_basic("김씨")
profile_basic("안씨")