

print('Доп задание 2')
class Student:
    def __init__(self, name, groupNumber, age):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getAge(self):
        print (f'Возраст ученика {self.name} равен {self.age}')

    def getName(self):
        print(f'Ученика зовут {self.name}')

    def getGroupNumber(self):
        print(f'Номер группы ученика {self.name} - {self.groupNumber}')

    def setNameAge(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
        print(f'Новые данные ученика:\nИмя: {self.name}\nВозраст: {self.age}')

    def setGroupNumber(self, new_groupNumber):
        self.groupNumber = new_groupNumber
        print(f'Новый номер группы ученика {self.name} - {self.groupNumber}')

# 5 students
Bob = Student('Bob', '9A', 16)
Max = Student('Max', '11C', 18)
Liza = Student('Liza', '9H', 17)
Karl = Student("Karl", "10B", 17)
Jack = Student('Jack', '11a', 18)

Bob.setGroupNumber('9B')
Max.getAge()
Liza.getName()
Karl.setNameAge('Kiril', '18')
Jack.getGroupNumber()


print('\nДоп задание 3')
class Math:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def addition(self):
        sum  = self.a + self.b
        print(f'Сумма чисел {self.a} и {self.b} равна {sum}')

    def multiplication(self):
        mult = self.a * self.b
        print(f'Произведение чисел {self.a} и {self.b} равна {mult}')

    def substraction(self):
        sub = self.a - self.b
        print(f'Вычитание чисел {self.a} и {self.b} равна {sub}')

    def division(self):
        if self.b != 0:
            div = self.a / self.b
            print(f'Вычитание чисел {self.a} и {self.b} равна {div}')
        else:
            print('Делить на ноль нельзя.')

nums = Math(7, 0)
nums.addition()
nums.multiplication()
nums.substraction()
nums.division()

print('\nДоп задание 4')
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен.')

    def off(self):
        print('Автомобиль заглушен.')

    def new_year(self, new_year):
        self.year = new_year
        print(f'{new_year} - Новый год выпуска машины.')

    def new_type(self, new_type):
        self.type = new_type
        print(f'{new_type} - новый тип автомобиля.')

    def new_color(self, new_color):
        self.color = new_color
        print(f'{new_color} - новый цвет автомобиля.')

lada = Car('green', 'picap', 2000)

lada.start()
lada.off()
lada.new_year(2000)
lada.new_type('cabriolet')
lada.new_color('red')




