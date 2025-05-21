
authorized = False

while not authorized:
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    if username == 'admin' and password == '1234':
        authorized = True
        print('Добро пожаловать!')
    else:
        print('Неверные данные, попробуйте снова.')