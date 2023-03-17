# 분기

weather = "rain"
if weather == "rain" or weather == "snow":
    print("우산을 챙기세요")
elif weather == "dust":
    print("마스크를 챙기세요")
else:
    print("그냥 나가세요")
    
temp = int(input("기온은 어떤가요?")) #input은 console창에 입력
if temp > 30:
    print("나가지 마세요")
elif temp <= 30 and temp >= 20:
# elif 30 >= temp >= 20:
    print("조금 더워요")
else:
    print("잘 모르겠어요")



