# Привести 7 примеров на List comprehension

# Пример 1 - числа в квадрате
print('Пример 1')
nums = range(1, 11)
print(f'Список чисел: {nums}')
num_kv = [i**2 for i in nums]
print(f'Числа в квадрате: {num_kv}')

# Пример 2 - числа умноженные на любое число пользователя
print('\nПример 2')
nums_2 = range(1, 11)
print(f'Список чисел: {nums_2}')
num_input = float(input('Введите любое число: '))
res = [i * num_input for i in nums_2]
print(f'Числа умноженные на {num_input}: {res}')

# Пример 3 - Печать только четных чисел
print('\nПример 3')
nums_3 = range(1, 11)
print(f'Список чисел: {nums_3}')
chet_nums = [i for i in nums_3 if i%2==0]
print(f'Четные числа: {chet_nums}')

# Пример 4 - печать только отрицательных чисел
print('\nПример 4')
nums_4 = range(-10, 11)
print(f'Список чисел: {nums_4}')
otr_nums = [i for i in nums_4 if i < 0]
print(f'Только отрицательные числа: {otr_nums}')

# Пример 5 - сложение strange
print('\nПример 5')
words = ['Book', 'kniga', 'Книга', 'книгА']
print(f'Список слов: {words}')
words_plus = [i +'два112' for i in words]
print(f'Сложение значений "str": {words_plus}')

# Пример 6 - Перебор значений for
print('\nПример 6')
nums_6 = range(1, 11)
res_6 = [i for i in nums_6]
print(f'Перебор значений: {res_6}')

# Пример 7 - Печать определенных слов с условиями
print('\nПример 7')
words = ['Book', 'kniga', 'Книга', 'книгА']
words_with_ = [i for i in words if 'а' in i ]
print(f'Слова только с русской буквой "а": {words_with_}')




