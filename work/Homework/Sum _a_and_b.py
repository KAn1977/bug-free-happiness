# Программа для сумирования двух чисел.

sum_nums = lambda x, y: x + y

while True:
    try:
        a = float(input('Введите первое число: '))
        break
    except ValueError:
        print('Введите число.')

while True:
    try:
        b = float(input('Введите второе число: '))
        break
    except ValueError:
        print('Введите число.')

print(f'\nСумма чисел {a} и {b} равна {sum_nums(a, b)}.')
