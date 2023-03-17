# 메서드 오버라이딩

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. 속도 : {2}".format(self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 : {2}".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))


class FlyUnit:
    def __init__(self, speed):
        self.speed = speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. 속도 : {2}".format(name, location, self.speed))


class AttackFlyUnit(AttackUnit, FlyUnit):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyUnit.__init__(self, speed)

    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)


vulture = AttackUnit("벌쳐", 80, 10, 20)
battleCruser = AttackFlyUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battleCruser.move("9시")


# 패스

class BuildingUnit(Unit): # 괄호 안의 클래스는 super의 대상이 된다.
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, location):
        super().__init__(name, hp, 0) # super를 통해 초기화 할 떄는 self를 삭제해야한다.
        self.location = location

supplyDepot = BuildingUnit("서플라이 디폿", 500, "7시")


# def gameStart():
#     print("새로운 게임을 시작합니다!")
#     pass # 아무것도 안하고 일단 넘어간다는 의미
#
#
# def gameOver():
#     pass
#
#
# gameStart()
# gameOver()
