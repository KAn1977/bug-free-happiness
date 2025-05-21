# Программа для определения палиндрома

# Приветствие

print('\t\t\tДобро пожаловать в программу для определения палиндромов.')

while True:   # Цикл
    # Ввод слова для проверки
    user_word = input('\nВведите любое слово: ')
    a = user_word.lower()
    b = user_word[-1::-1].lower()

    # Вывод
    if user_word == "123":
        print('Пока!')
        break
    elif a == b:
        print(f'Ваше слово "{user_word}" - палиндром')
    elif a != b:
        print(f'Ваше слово "{user_word}" - не палиндром')
    elif user_word == 123:
        print('Пока!')
        break
