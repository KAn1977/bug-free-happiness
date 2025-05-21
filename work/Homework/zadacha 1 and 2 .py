print('Задание 1.')
class Man:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        print(f'Возраст {self.name} равен {self.age}.')

    def newAge(self, new_age):
        self.age = new_age
        print(f'Новый возраст ученика {self.name} равен {self.age}.')

    def newName(self, new_name):
        self.name = new_name
        print(f'Новое имя ученика - {self.name}')


Bob = Man('Bob', 18)
Bob.getAge()
Bob.newAge(20)
Bob.newName('Max')


print('\nЗадание 2.')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


alan = Person('Alan', 34)
liza = Person('Liza', 18)
din = Person('Din', 8)


print(f'Общая информация о {alan.name}:\n name = {alan.name}\n age = {alan.age}')
print(f'\nОбщая информация о {liza.name}:\n name = {liza.name}\n age = {liza.age}')
print(f'\nОбщая информация о {din.name}:\n name = {din.name}\n age = {din.age}')





