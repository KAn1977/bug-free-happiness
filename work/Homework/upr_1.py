# Упражнения 1-4

# Упражнение 1
print('Упражнение 1\n')
print('Николай')
print('Почтоый адрес - 100123')


# Упражнение 2
print('\nУпражнение 2')
user_name = str(input('\nВведите ваше имя: '))
print(f'Приветствую вас, {user_name.title()}!')


# Упражнение 3
print('\nУпражнение 3')
a = float(input(f'\nВведите длину комнаты (в метрах): '))  # Задать вопрос на уроке
b = float(input('Введите ширину комнаты (в метрах): '))
x = a * b # Площадь
print(f'Площадь комнаты: {x} квадратных метров')


# Упражнение 4
print('\nУпражнение 4')
q = float(input('\nВведите длину сада (в футах): '))  # Задать вопрос на уроке
w = float(input('Введите ширину сада (в футах): '))
y = q * w # Вычисление площади в квадратных футах
y_acres = y / 43560 # Перевод площади в арки
print(f'Площадь участка: {y_acres:} акр(а)')

