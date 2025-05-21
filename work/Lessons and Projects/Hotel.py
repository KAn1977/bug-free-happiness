# Hotel sistem
clients = {}
free_rooms = [i for i in range(1, 21)]
close_rooms = []

# Функция Добавление клиента в список
def add_cl(name, room):
    if name not in clients:
        clients[name] = room
        free_rooms.remove(room)
        close_rooms.append(room)
        print(f'Клиент {name} заселен в комнату {room}.')
        print(f'Свободные комнаты: {free_rooms}')
    else:
        print(f'Клиент {name} уже заселен.')

# Функция Удаление клиента из списка
def del_cl(name, room):
    if name in clients:
        clients.pop(name)
        close_rooms.remove(room)
        free_rooms.append(room)
        print(f'Клиент {name} выселен из комнаты {room}.')
        print(f'Свободные комнаты: {free_rooms}')
    else:
        print(f'Клиента {name} нет в списке.')

# Функция Показ занятых номеров
def show_close_rooms():
    print(f'Занятые номера: {close_rooms}')

# Начало работы программы
# Приветствие и предоставление функционала программы
print('\t\t\tДобро пожаловать в "BigBrotherWatch".')
while True:
    print('\nВы можете: \n1 - Просмотреть свободные номера.\n2 - Просмотреть занятые номера.\n3 - Добавить клиента.'
          '\n4 - Удалить клиента.\n5 - Закрыть программу. ')

    admin_inp = int(input('\nВведите  цифру действия: '))

    if admin_inp == 1:
        print(f'Свободные номера: {free_rooms}.')

    elif admin_inp == 2:
        show_close_rooms()

    elif admin_inp == 3:
        cl_name = input('Введите имя клиента: ').title().strip()
        cl_room = int(input('Введите номер комнаты: ').strip())
        add_cl(cl_name, cl_room)

    elif admin_inp == 4:
        cl_name = input('Введите имя клиента: ').title().strip()
        cl_room = int(input('Введите номер комнаты: ').strip())
        del_cl(cl_name, cl_room)

    elif admin_inp == 5:
        print('Закрытие программы.')
        break



