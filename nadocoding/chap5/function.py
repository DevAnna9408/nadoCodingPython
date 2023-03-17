# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission # 파이썬은 리턴에 두 개를 넣을 수 도 있다..

balance = 0
balance = deposit(balance, 1000)
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
commision, balance = withdraw_night(balance, 500) # 리턴을 두 개를 받았기 때문에, 할당 할 때도 콤마로 구분해서 두 개를 넣어준다.
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commision, balance))