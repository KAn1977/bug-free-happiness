


class Animal:

    def make_sound(self):
        crew = 'aaaaaa'
        print(crew)
        return crew



class Dog(Animal):

    def make_sound(self):
            print('Gaw')

class Cat(Animal):

    def make_sound(self):
            print('Myau')

class Cow(Animal):

    def make_sound(self):
            print('Moooo')

dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound()


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f'Информация по вашей машине:\nБрэнд машины - {self.brand}.'
                                            f'Год выпуска - {self.year}.')

class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def display_info(self):
        print(f'\nИнформация по вашей машине:\nБрэнд машины - {self.brand}.'
                                            f' Год выпуска - {self.year}.'
                                            f' Цвет машины - {self.color}.')


class Motorcycle(Vehicle):
    def __init__(self, brand, year, power):
        super().__init__(brand, year)
        self.power = power

    def display_info(self):
        print(f'\nИнформация по вашей машине:\nБрэнд машины - {self.brand}.'
                                            f' Год выпуска - {self.year}.'
                                            f' Мощность машины - {self.power}.')


song_plus = Car('BYD', 2024, 'white')
rebel = Motorcycle('Honda', 2022, '1100hp')
song_plus.display_info()
rebel.display_info()


