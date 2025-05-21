class School: #создание пустого класса.
    pass

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

BYD_1 = Car('Song Plus','Grey', 2024)
print(BYD_1.model.upper())
print(BYD_1.color.lower())
print(BYD_1.year)


class User:
    def __init__(self, name):
        self.name = name

user1 = User('Bob')
print(user1.name)


class Man:
    def __init__(self,name, age, job, color):
        self.name = name
        self.age = age
        self.job = job
        self.color = color

bob = Man('Jack', 'Aged 10', 'School', 'White')
print(vars(bob))
print(vars(bob), user1.name)



