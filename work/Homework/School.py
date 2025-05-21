# School managment system

admins = {'BigDaddy' : 'Zarplata',                          # Логины / Пароли админов
          'Dog' : 'Cat',
          'Bambook' : '12345asd'}

students = {}# 'Bob' : 3                                     # Словарь учеников
classes = [i for i in range(1, 4)]                           # Кол - во классов
cl_1, cl_2, cl_3 =[],[],[]

# Фунцкия Все опции программы
def options():

    print('\nВы можете: \n1 - Показать все классы.\n2 - Добавить ученика.'
          '\n3 - Удалить ученика.\n4 - Найти информацию по ученику.\n5 - Показать всех студентов.\n6 - Закрыть программу. ')


# Функция (1) Осмотр всех классов.
def all_classes():
    print(f'Все классы школы:\n1-ый класс:{cl_1}\n2-ой класс:{cl_2}\n3-ий класс:{cl_3}')


# Функция Проверка на вместимость класса.
def check_people_in_class(name,clas):
    if clas not in range(1,4):
        print(f'Класса {clas} нет в нашей школе.')
        return
    elif clas == 1:
        if len(cl_1) < 5:
            cl_1.append(name)
            students[name] = 1
            print(f'Ученик {name} добавлен в 1 класс.')
            print(f'Текущий состав класса №1: {cl_1}')
        elif len(cl_1)  == 5:
            print(f'Класс {clas} заполнен.')
    elif clas == 2:
        if len(cl_2) < 5:
            cl_2.append(name)
            students[name] = 2
            print(f'Ученик {name} добавлен в 2 класс.')
            print(f'текущий состав класса №2: {cl_2}')
        elif len(cl_2)  == 5:
            print(f'Класс {clas} заполнен.')
    elif clas == 3:
        if len(cl_3) < 5:
            cl_3.append(name)
            students[name] = 3
            print(f'Ученик {name} добавлен в 3 класс.')
            print(f'текущий состав класса №3: {cl_3}')
        elif len(cl_3)  == 5:
            print(f'Класс {clas} заполнен.')


# Функция (2) Добавление ученика в класс
def add_st(name, clas):
    if name in students:
        print(f'Студент {name} уже учится {students[name]} классе.')
    else:
        check_people_in_class(name, clas)


# Функция (3) Удаление ученика из класса.
def del_st(name):
    if name in students:
        if students[name] == 1:
            cl_1.remove(name)
            students.pop(name)
            print(f'Ученик {name} удален из 1 класса.')
            print(f'текущий состав класса №1: {cl_1}')
        elif students[name] == 2:
            cl_2.remove(name)
            students.pop(name)
            print(f'Ученик {name} удален из 2 класса.')
            print(f'текущий состав класса №2: {cl_2}')
        elif students[name] == 3:
            cl_3.remove(name)
            students.pop(name)
            print(f'Ученик {name} удален из 3 класса.')
            print(f'текущий состав класса №3: {cl_3}')
    else:
        print(f'Ученик {name} не учится в нашей школе.')


# Функция (4) Найти информацию ученика
def search_st (name):
    if name in students:
         print(f'Ученик {name} учится в {students[name]} классе.')
    else:
         print(f'Ученик {name} не учится в нашей школе.')



# Авторизация админа

print('Авторизация')
active = False
while not active:

    login = str(input('Введите логин: '))
    password = str(input('Введите пароль: '))

    if login in admins.keys() and password == admins[login]:
        print(f'\t\t\t\nДобро пожаловать в систему "BigBrotherWatch", {login}.')
        active = True
    elif login in admins.keys() and password != admins[login]:
        print('Неверный пароль.')
    elif login not in admins.keys():
        print('Неверный логин.')

# Приветствие и предоставление функционала программы
while True:
    options()
    try:
        num = int(input('\nВведите номер действия: '))
    except ValueError:
        print('Вы ввели не номер.')
        continue
    if num == 1:
        all_classes()

    elif num == 2:
        name = input('Введите имя: ').strip().title()
        try:
            clas = int(input('Введите номер класса: '))
        except ValueError:
            print('Вы ввели не номер.')
            continue
        add_st(name, clas)

    elif num == 3:
        name =str(input('Введите имя ученика: ')).strip().title()
        del_st(name)

    elif num == 4:
        name = str(input('Введите имя ученика: ')).strip().title()
        search_st(name)

    elif num == 5:
        print(students)

    elif num == 6:
        print('Досвидание.')
        break

    elif num != range(1, 7):
        print('Такого действия нет.')













