# # 스타크래프트를 예로 드는 클래스
#
# name = "marin"
# hp = 40
# damage = 5
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}".format(hp, damage))
#
# tank_name = "tank"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}".format(tank_hp, tank_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 시 방향으로 적군을 공격합니다. 공격력은 {2} 입니다.".format(name, location, damage))
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
#
#

class Unit:
    def __init__(self, name, hp): ## __init__은 생성자이다.
        self.name = name #클래스 내에서 정의 된 변수를 멤버 변수라고 한다. 코틀린의 멤버 프로퍼티
        self.hp = hp

marine1 = Unit("마린", 40)
marine2 = Unit("마린", 40)
tank = Unit("시즈", 150)

wraith1 = Unit("레이스", 80)
print("유닛 이름: {0}".format(wraith1.name)) # getter 처럼 꺼내쓸 수 있다.

wraith2 = Unit("레이스", 80)
wraith2.clocking = True # 파이썬에서는 클래스에 세터를 마음대로 추가할 수 있다..

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 메서드와 상속

class AttackUnit(Unit): # 괄호 안에 클래스를 넣으면 상속 받는다는 의미다
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스를 불러온 다음 init 문을 사용해 생성자를 만든다.
        self.damage = damage # 상속 받은 후 멤버 프로퍼티를 추가한다.

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 : {2}".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

# 다중 상속

class FlyUnit:
    def __init__(self, speed):
        self.speed = speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. 속도 : {2}".format(name, location, self.speed))

class AttackFlyUnit(AttackUnit, FlyUnit): # 괄호 안에 두 가지 이상을 넣으면 다중 상속이 된다.
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, damage)
        FlyUnit.__init__(self, speed)

valkiri = AttackFlyUnit("발키리", 200, 60, 5)
valkiri.fly(valkiri.name, "3시")


