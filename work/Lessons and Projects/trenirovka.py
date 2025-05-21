active = True
while active:
    try:
        age = int(input('Введите ваш возраст: '))
        active = False
    except ValueError:
        print('Вы ввели не число.')
