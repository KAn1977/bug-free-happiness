# Приветствие.
print('\nДобро пожаловать, игроки. Сегодня мы поиграем в игру "Камень - Ножницы - Бумага".\n')

# Ввод никнейма игроков.
player_1 = input('Введите ваш никнейм: ')
player_2 = input('Введите ваш никнейм: ')

# Правила игры.
print('\nПравила игры:\n\n 1) Играют два человека\n 2) Каждый игрок выбирает один из трех жестов:\n\n - Камень\n - Ножницы\n - Бумага\n')
print('Кто кого побеждает:\n\n - Камень бьёт ножницы\n - Ножницы бьют бумагу\n - Бумага бьёт камень\n - Одинаковые жесты — ничья\n')

# Жесты.
Rock = 'Камень'
Paper = 'Бумага'
Scissors = 'Ножницы'

# Ввод жестов игроками.
run_player_1 = input(f'{player_1}, введите ваш жест: ').strip().title()
run_player_2 = input(f'{player_2}, введите ваш жест: ').strip().title()

# Определение победителя или ничья.
err = None #Для работы концовки
if run_player_1 == run_player_2:
    print('\nНичья.\nGAME OVER!')
elif run_player_1 == Rock and run_player_2 == Scissors:
    print(f'\n{Rock} бьет жест {Scissors}.')
    print(f'Игрок {player_1} Победил!!!')
elif run_player_1 == Rock and run_player_2 == Paper:
    print(f'\n{Paper} бьет жест {Rock}.')
    print(f'Игрок {player_2} Победил!!!')
elif run_player_1 == Paper and run_player_2 == Rock:
    print(f'\n{Paper} бьет жест {Rock}.')
    print(f'Игрок {player_1} Победил!!!')
elif run_player_1 == Paper and run_player_2 == Scissors:
    print(f'\n{Scissors} бьет жест {Paper}.')
    print(f'Игрок {player_2} Победил!!!')
elif run_player_1 == Scissors and run_player_2 == Paper:
    print(f'\n{Scissors} бьет жест {Paper}.')
    print(f'Игрок {player_1} Победил!!!')
elif run_player_1 == Scissors and run_player_2 == Rock:
    print(f'\n{Rock} бьет жест {Scissors}.')
    print(f'Игрок {player_2} Победил!!!')
else:
    err = 'Введены неправильные жесты.\nПопробуйте еще раз.'
    print(f'\n{err}')

# Концовка.
if err is None:
    print('\nСпасибо за игру! До новых встреч!')
