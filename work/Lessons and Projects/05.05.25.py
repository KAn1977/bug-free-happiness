usernames = []
while True:
    inname = input('Введите имя: '.title())

    if inname in usernames:
        print(f'Имя {inname} уже есть в списке. Попробуйте добавить другое имя.')
        usernames.sort()
        print(f'\nВаш лист имен: {usernames}')
    else:
        usernames.append(inname.title())
        usernames.sort()
        print(f'\nВаш лист имен: {usernames}')


