# 1. Сделать приложение (список контактов)
# - в приложение должно присутствовать удаление, изменение, добавление контактов
# - дополнительные библиотеки не нужны

# Приветствие.
print('\t\t\tДобро пожаловать в ваш список контактов\n')

# Список контактов
contacts = ['Bob', 'Anna', 'Bruce', 'Oleg']
contacts.sort()

while True:
    print('Вы можете:')
    print('1 - Удалить контакт.')
    print('2 - Изменить контакт.')
    print('3 - Добавить контакт.')
    print('4 - Очистить список контактов.')
    print('5 - Показать список контактов.')
    print('0 - Выйти из программы.')

    go = int(input('\nЧто вы хотите сделать: '))

    # Удаление контакта
    if go == 1:
        name_del = input('Какой контакт вы хотите удалить: ').title()
        if name_del in contacts:
            contacts.remove(name_del)
            print(f'\nКонтакт {name_del} удален.')
            print(f'\nНовый список контактов: {contacts}')
        else:
            print('Данного контакта нет в списке ')

            # Изменение контакта на другой контакт
    elif go == 2:
        change_name = input('Какой контакт вы хотите изменить: ').title()
        if change_name in contacts:
            new_name = input('Введите новое имя контакта: ').title()
            contacts.remove(change_name)
            contacts.append(new_name)
            contacts.sort()
            print(f'\nНовый список контактов:\n{contacts}')
        else:
            print(f'\nКонтакта {change_name} нет в списке.')
            print(f'\nСписок контактов:\n{contacts}')

    # Добавление нового контакта
    elif go == 3:
        name_add = input('Какой контакт вы хотите добавить: ').title()
        if name_add in contacts:
            print('Такой контакт уже есть!')
        else:
            contacts.append(name_add)
            contacts.sort()
            print(f'\nКонтакт {name_add} добавлен.')
            print(f'\nНовый список контактов:\n{contacts}')

    # Очистка списка
    elif go == 4:
        contacts.clear()
        print(f'\nНовый список контактов: {contacts}')

    # Текущий список контактов
    elif go == 5:
        print(f'\nТекущий список контактов:\n{contacts}')

    # Выход из программы
    elif go == 0:
        print('Выход из программы. До свидания!')
        break

    else:
        print('Неизвестная команда!')