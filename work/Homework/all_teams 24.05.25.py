# Урок 2 - Переменные, типы данных, условные и  математические операторы.

"""
Переменные str int and float
"""

while True:
    num_str_input = input('Введите что угодно: ')
    num_int = 12
    num_float = 12.21

    if num_str_input == '1':
     print(f'Умножение: {num_int * num_float}')
    elif num_str_input =='2':
        print(f'Деление: {num_int / num_float}')
    else:
        print(num_int > num_float) #True - False
        break


 # Урок 3 - Списки, кортежи и их методы

nums = [1,2,3,4,5,6,7,8,9,10]
nums_kort = (1,2,3,4,5,6,7,8,9,10)

print(f'\n{nums[0]}')  # first number in list
print(nums[-1]) # last number in list

# Добавление в список
nums.append('asd')
nums.insert(0,0)
nums.extend([11,12,13])
print(nums)

# Удаление в списках
nums.pop()
nums.pop(0)
nums.remove('asd')

nums.reverse()
print(nums)
print(nums[0:11:2])


"""
Кортеж - это такой же список с такими же методами, но он относится к неизменяемой структуре данных.
"""

# Урок 4-5 Цикл и List comprehension
while True:
    try:
        choice =int(input('\nВведите число от 1 до 2: '))
    except ValueError:
        print('Вы ввели не число.')
        continue

    arif = [1,2,3,4,5]
    if choice == 1:
        stepen = [i**2 for i in arif]
        print(stepen)

    elif choice == 2:
        vivod = [i for i in arif ]
        print(vivod)
    else:
        print('└┴║╣╗┐╝║\n')
        break


# Урок 6 Словарь и сеты
kitchen = {'table' : 1,
           'chair' : 8,
           'plaid' : 15,
           'fork' : 15,
           'spoon' : 15}

for i in kitchen.values():
    print(i)

for i in kitchen.keys():
    print(i.title())

for i in kitchen.items():
    print(i)

kitchen['table'] = 3
print(kitchen)

"""
Сет = это набор неповторяющихся значений - если в сете есть повторяющиеся элементы в списке, то при выводе списка 
выводятся только сортированные элементы без повторений.
"""

letter = {'a', 'a', 'b', 'b', 'c', 'c','d', 'd'}
print(letter)

# Урок 7 Функции

def spisok (*a):
    print(f'\nСписок: {a}')

spisok('apple', 'citrus', 'watermelon', 'pineapple', 'cherry')


# Урок 8 Lambda
x = lambda y: y**2
print(f'\n{x(10)}\n')

# Урок 9 - 10 Суперкласс и подкласс

class Human():
    def __init__(self, age, height, weight, color):
        self.age = age
        self.height = height
        self.weight = weight
        self.color = color

    def eat(self):
        print('Nyam nyam nyam')

class Baby(Human):
    def __init__(self, age, height, weight, color, hair):
        super().__init__( age, height, weight, color)
        self.hair = hair

bob = Baby(18, 177, 70, 'white', 'blond')
bob.eat()

