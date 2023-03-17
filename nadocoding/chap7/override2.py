class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FltableUnit(Unit, Flyable): # 다중 상속을 받을 때 super의 대상은 첫 번째가 된다.
    def __init__(self):
        super().__init__()

dropship = FltableUnit()