# Интернет - магазин

# 1. Улучшить интернет-магазин
# - должна присутствовать корзина
# - замена товаров в корзине
# - удаление товаров
# - доп библиотека не требуются

# Словарь и корзина
all_products = {'Весь склад': {'Potato': 16_000,
                               'Tomato': 12_000,
                               'Apple': 10_000,
                               'Banana': 8_000,
                               'Lemon': 6_000,
                               'Grape': 4_000}
                }
korz = {}

# Приветствие
print('\t\t\tДобро пожаловать в магазин "Teleshka".')
while True:
    print('\nЧто вы хотите сделать?'
          '\n1 - Добавить продукт на склад.\n2 - Показать остатки склада.\n3 - Добавить продукт в корзину.'
          '\n4 - Показать корзину.\n5 - Убрать продукт из корзины.\n6 - Заменить продукт в корзине.'
          '\n7 - Удалить товар из склада.''\n8 - Закрыть программу.')

    user_inp = int(input('\nВведите номер действия: '))

    # Добавление нового продукта в склад
    if user_inp == 1:
        product_name = input('\nВведите название продукта: ').strip().title()
        product_nums = int(input('Введите количество: ').strip())
        if product_name in all_products['Весь склад']:                  # Если товар уже есть на складе
            all_products['Весь склад'][product_name] += product_nums
            print(f'Остатки на складе: {all_products}')
        else:                                                            # Если товара нет на складе
            all_products['Весь склад'][product_name] = product_nums
            print(f'Остатки на складе: {all_products}')

    # Актуальные остатки склада
    elif user_inp == 2:
        print('\nАктуальные остатки:')
        for k, v in all_products['Весь склад'].items():
            print(f'{k} - {v}')

    # Закрытие программы
    elif user_inp == 8:
        print('\t\t\tВсего доброго.')
        break

    # Добавление продукта в корзину
    elif user_inp == 3:
        print('\n1 - Добавить в корзину.\n2 - Закрыть корзину')
        user_3 = int(input('\nВведите номер варианта: '))

        if user_3 == 2:                                                  # Закрытие корзины
            print('')
        elif user_3 == 1:                                                # Добавление товара в корзину
            print('\nАктуальные остатки:')
            for k, v in all_products['Весь склад'].items():              # Показывает пользователю весь остатки склада
                print(f'{k} - {v}')
            user_3_pr_input = input('\nВыберете продукт: ').strip().title()
            user_3_nums_input = int(input('Выберете количество: '))

            if user_3_pr_input in all_products['Весь склад']:            # Проверка наличия товара на складе
                if user_3_nums_input > all_products['Весь склад'][user_3_pr_input]: # Если недостаточно товара на складе
                    print(f'Недостаточно {user_3_pr_input} на складе.')
                elif user_3_pr_input in korz and user_3_nums_input <= all_products['Весь склад'][user_3_pr_input]:   # Если товар уже есть в корзине
                    korz[user_3_pr_input] += user_3_nums_input
                    all_products['Весь склад'][user_3_pr_input] -= user_3_nums_input
                    print(f'\nВаша текущая корзина: {korz}')
                elif user_3_pr_input in korz and user_3_nums_input > all_products['Весь склад'][user_3_pr_input]:
                    print(f'Недостаточно {user_3_pr_input} на складе.')
                else:
                    korz[user_3_pr_input] = user_3_nums_input
                    # Новые остатки корзины
                    print(f'\nВаша текущая корзина: {korz}')

                    # Новые остатки на складе
                    all_products['Весь склад'][user_3_pr_input] -= user_3_nums_input
                    print(f'Остатки на складе: {all_products["Весь склад"]}')
            else:
                print(f'\nПродукта {user_3_pr_input} нет на складе.\nХотите добавить этот товар на склад ?\n1 - "Да"\n2 - "Нет"')
                choice_3 = int(input('Введите число: '))
                if choice_3 == 1:
                    all_products['Весь склад'][user_3_pr_input] = user_3_nums_input
                else:
                    print(f'')

    # Показ актуальной корзины
    elif user_inp == 4:
        print(f'Ваша корзина: {korz}')

    # Удаление товара из корзины
    elif user_inp == 5:
        print(f'\nВаша корзина: {korz}')
        del_korz = input('Выберите товар, который хотите удалить из корзины: ').strip().title()
        if del_korz in korz:
            all_products['Весь склад'][del_korz] += korz[del_korz]
            korz.pop(del_korz)
        else:
            print(f'{del_korz} нет в вашей корзине.')

    # Замена товара в корзине
    elif user_inp == 6:
        print(f'\nВаша корзина: {korz}')
        old_prod_input = input('Введите товар, который вы хотите заменить: ').strip().title()
        new_prod_input = input('Введите новый товар: ').strip().title()
        new_prod_num = int(input('Какое количество вам нужно: '))
        if old_prod_input in korz and new_prod_input in all_products['Весь склад'] and all_products['Весь склад'][new_prod_input] >= new_prod_num:
            all_products['Весь склад'][old_prod_input] += korz[old_prod_input] # Возращение товара из корзинки на склад
            del korz[old_prod_input]
            korz[new_prod_input] = new_prod_num                            # Замена старого товара на новый
            all_products['Весь склад'][new_prod_input] -= new_prod_num
        elif all_products['Весь склад'][new_prod_input] < new_prod_num:
                print(f'Недостаточно {new_prod_input} на складе.')
        elif new_prod_input not in all_products['Весь склад']:
            print(f'\n{new_prod_input} нет на складе\nХотите добавить этот товар на склад ?\n1 - "Да"\n2 - "Нет"')
            choice_6 = int(input('Введите число: '))
            if choice_6 == 1:
                all_products['Весь склад'][new_prod_input] = new_prod_num
        else:
            print(f'{old_prod_input} нет в корзине.')

    # Удаление товара из склада
    elif user_inp == 7:
        print(all_products['Весь склад'])
        del_prod = input('\nНапишите товар, который вы хотите удалить из склада: ').strip().title()
        if del_prod in all_products['Весь склад']:
            all_products['Весь склад'].pop(del_prod)
        else:
            print(f'{del_prod} нет на складе.')

    else:
        print('Введено неверное значение. Попробуйте еще раз.')