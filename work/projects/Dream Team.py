class DreamTeam:
    def __init__(self, speed  , power  , stamina  , accuracy):
        self.speed = speed
        self.power = power
        self.stamina = stamina
        self.accuracy = accuracy

class First(DreamTeam):
    def __init__(self, speed  , power  , stamina  , accuracy):
        super().__init__( speed  , power  , stamina  , accuracy)
    def attack(self):
        print('Удар')

class Second(DreamTeam):
    def __init__(self, speed  , power  , stamina  , accuracy):
        super().__init__( speed  , power  , stamina  , accuracy)
    def deffend(self):
         print('Прессинг')

class Thierd(DreamTeam):
    def __init__(self, speed  , power  , stamina , accuracy):
        super().__init__( speed  , power , stamina  , accuracy)
    def passs(self):
        print('Пас')

class Four(DreamTeam):
    def __init__(self, speed  , power , stamina , accuracy):
        super().__init__( speed  , power  , stamina  , accuracy)
    def cathc(self):
        print('Ловить')


bob = First('100','100','100','100')
max = Second('100','100','100','100')
sam = Thierd('100','100','100','100')
jack = Four('100','100','100','100')

bob.attack()
max.deffend()
sam.passs()
jack.cathc()



