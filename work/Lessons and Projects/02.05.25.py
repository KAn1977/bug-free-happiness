# Списки
names = []
nums = []
off = []

# Ввод пользователем номера
while True:
    print('Вы можете:\n1 - Ввести новое имя.\n2 - Ввести новый номер.\n3 - Ввести новую услугу.\n4 - Закрыть программу.\n5 - показать все списки.')
    user_ch = (str(input('Что вы хотите сделать: ')))

    #
    if user_ch == '2':
        new_num = input('Введите новый номер: ')
        nums.append(new_num)
    elif user_ch == '1':
        new_name = input('Введите новое имя: ')
        names.append(new_name)
    elif user_ch == '3':
        new_off = input('Введите новую услугу: ')
        names.append(new_off)
    elif user_ch == '4':
        print('Всего вам доброго.')
        break
    elif user_ch == '5':
        print(names)
        print(nums)
        print(off)












