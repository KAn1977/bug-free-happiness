# ГЛАВА 2 - ПЕРЕМЕННЫЕ И ПРОСТЫЕ ТИПЫ ДАННЫХ

"""
2-3. Личное сообщение: сохраните имя пользователя в переменной и выведите сообщение,
предназначенное для конкретного человека.

2-4. Регистр символов в именах: сохраните имя пользователя в переменной и выведите его
в нижнем регистре, в верхнем регистре и с капитализацией.

2-5. Знаменитая цитата: найдите известное высказывание. Выведите цитату и имя её автора.

2-7. Удаление пропусков: сохраните имя человека в переменной, включающей пропуски в начале и конце.
Выведите имя с использованием каждого символа пропуска (\t и \n), затем удалите пропуски.
"""


# Ваши решения для главы 2:



# ГЛАВА 3 - СПИСКИ

"""
3-1. Имена: сохраните имена нескольких своих друзей в списке и выведите каждое имя, обращаясь 
к каждому элементу списка по отдельности.

3-2. Сообщения: начните со списка из упражнения 3-1. Выведите сообщение для каждого человека.

3-4. Список гостей: создайте список с именами гостей, приглашаемых на обед. Выведите каждому гостю 
персональное приглашение на обед.

3-5. Изменение списка гостей: один из гостей прийти не сможет. Добавьте в программу строку с его именем 
и сообщение о том, что он не придет. Замените имя гостя именем нового приглашенного.

3-7. Сокращение списка гостей: только что выяснилось, что новый обеденный стол привезти вовремя не успеют.
Удалите гостей из списка, пока не останется только два имени.
"""

# Ваши решения для главы 3:
friends = ['bob', 'jack', 'max']
print(f'Hi, {friends[0].title()}')
for i in friends:
    print(f'{i.title().strip()}, hello')

friends.append('sam')
friends.insert(12,'oleg')
friends.sort()

print(f'\n{friends}')

new_friend = 'liza'
friends[-1] = new_friend
print(f'\n{friends}')


print(friends)
friends.pop()
del friends[0]
friends.remove('jack')
print(friends)

# ГЛАВА 4 - РАБОТА СО СПИСКАМИ

"""
4-1. Пицца: создайте список из трех видов пиццы. Выведите все названия пицц в цикле for.

4-2. Животные: создайте список из трех животных. Выведите названия всех животных в цикле for.
Добавьте строку с общей характеристикой этих животных.

4-3. Считаем до 20: используйте цикл for для вывода чисел от 1 до 20 включительно.

4-5. Суммирование: создайте список чисел от 1 до 1 000 000 и используйте min() и max() 
для проверки списка. Также найдите сумму всех чисел.

4-8. Кубы: создайте список первых 10 кубов (куб числа x — это значение x**3) и выведите все значения.
"""

# Ваши решения для главы 4:
all_nums = list(range(1,1_000_001))
print(all_nums)
print(sum(all_nums))

kubs = [i**3 for i in range(1,11)]
print(kubs)




# ГЛАВА 5 - КОМАНДЫ IF

"""
5-1. Проверка условий: напишите последовательность условий. Выведите описание каждой проверки 
и результат ее оценки.

5-3. Цвета 1: представьте, что вы только что купили велосипед, и хотите добавить его в список.
Напишите команду if для проверки того, что в списке присутствует определенный цвет.

5-6. Периоды жизни: напишите цепочку if-elif-else для определения периода жизни человека. 
Присвойте значение переменной age и выведите соответствующее сообщение.

5-8. Hello Admin: создайте список из 5 пользователей, включающий имя 'admin'. 
Выведите приветствие для каждого пользователя.
"""

# Ваши решения для главы 5:



# ГЛАВА 6 - СЛОВАРИ

"""
6-1. Человек: создайте словарь с информацией об известном вам человеке. Выведите каждый фрагмент 
информации, хранящийся в словаре.

6-2. Любимые числа: используйте словарь для хранения любимых чисел. Выведите каждое число.

6-3. Глоссарий: создайте словарь с пятью терминами программирования. Выведите каждое слово и его 
определение.

6-5. Реки: создайте словарь, в котором ключами будут названия рек, а значениями — страны, 
по которым протекает река. Выведите названия всех рек, всех стран, и каждую пару река—страна.
"""

# Ваши решения для главы 6:
man = {'sex' : 'man', 'age' : 16, 'job' : 'cleaner'}
print(man)





# ГЛАВА 7 - ВВОД ДАННЫХ И ЦИКЛЫ WHILE

"""
7-1. Прокат машин: запросите у пользователя, какую машину он хотел бы взять напрокат, 
и выведите соответствующее сообщение.

7-2. Заказ стола в ресторане: спросите пользователя, на сколько мест он хо��ет забронировать стол. 
Если заказано больше 8 мест, сообщите, что придется подождать.

7-3. Числа, кратные 10: запросите число и сообщите, кратно оно 10 или нет.

7-5. Билеты в кино: напишите цикл, который спрашивает возраст посетителя и выводит стоимость билета.
"""

# Ваши решения для главы 7:
act = True
while act:
    cor_num = int(input(('Введите число: ')))
    if cor_num%10 == 0:
        print('good')
        act = False

    else:
        print('not good')

while True:
    try:
        num = int(input('Введите число: '))
        break

    except ValueError:
        print('Вы ввели str.')



# ГЛАВА 8 - ФУНКЦИИ

"""
8-1. Сообщение: напишите функцию display_message(), которая выводит сообщение о том, что вы изучаете 
в этой главе.

8-2. Любимая книга: напишите функцию favorite_book(), которая получает параметр title и выводит 
сообщение.

8-3. Футболка: напишите функцию make_shirt(), которая получает размер футболки и текст, который должен 
быть напечатан на ней.

8-5. Города: напишите функцию describe_city(), которая получает название города и страну. 
Функция должна выводить простое сообщение.

8-7. Альбом: напишите функцию make_album(), которая строит словарь с описанием музыкального альбома.
"""

# Ваши решения для главы 8:

