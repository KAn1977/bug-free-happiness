# Интернет - магазин

#1. Улучшить интернет-магазин
# - должна присутствовать корзина
# - замена товаров в корзине
# - удаление товаров
# - доп.библиотеки не требуются


# Словарь и корзина
all_products = {'Весь склад' : {'Potato': 16_000, 'Tomato': 12_000, 'Apple': 10_000, 'Banana': 8_000, 'Lemon': 6_000, 'Grape': 4_000,}}
korz = {}

# Приветствие
print('\t\t\tДобро пожаловать в магазин "Teleshka".')
while True:
     print('\nЧто вы хотите сделать ?\n1 - Добавить продукт в склад.\n2 - Показать остатки склада.\n3 - Добавить продукт в коризну.\n4 - Показать корзину.\n5 - Убрать продукт из корзины.\n6 - Заменить продукт в корзине.\n7 - Закрыть программу.')
     user_inp = int(input('\nВведите номер варианта: '))

     # Добавление нового продукта в склад
     if user_inp == 1:
         product_name = (input('Введите название продукта: ').strip().title())
         product_nums = int(input('Введите количество: ').strip())
         all_products['Весь склад'][product_name] = product_nums
         print(f'Остатки: {all_products}')

     # Актуальные остатки склада
     elif user_inp == 2:
         print('Актуальные остатки:')
         for k,v in all_products['Весь склад'].items():
             print(f'{k} - {v}')

     # Закрытие программы
     elif user_inp == 7:
         print('\t\t\tВсего доброго.')
         break

     # Добавление продукта в корзину
     elif user_inp == 3:
         print('\n1 - Добавить в корзину.\n2 - Закрыть корзину')
         user_3 = int(input('\nВведите номер варианта: '))

         if user_3 == 2: # Закрытие корзины
             print('')
         elif user_3 == 1: # Добавление товара в корзину
             print('\nАктуальные остатки:')
             for k, v in all_products['Весь склад'].items():  # Показывает пользователю весь остатки склада
                 print(f'{k} - {v}')
             user_3_pr_input = str(input('\nВыберете продукт: ').strip().title())
             user_3_nums_input = int(input('Выберете кол - во: '))
             if user_3_pr_input in all_products['Весь склад']: # Проверка наличия товара на складе
                 if user_3_nums_input > all_products['Весь склад'][user_3_pr_input]: # Если недостаточно товара на складе
                     print(f'Недостаточно {user_3_pr_input} на складе.')
                else:
              korz[user_3_pr_input] = [user_3_nums_input,]
                     # Новые остатки корзины

                    print(f'\nВаша текущая корзина: {korz}')

                    # Новые остатки на складе
                    new_znach = all_products['Весь склад'][user_3_pr_input] - user_3_nums_input
                    all_products['Весь склад'][user_3_pr_input] = new_znach
                    print(f'Остатки на складе: {all_products['Весь склад']}')

             else:
                 print(f'\nПродукта {user_3_pr_input} нет на складе.')
                 a = (all_products['Весь склад'][user_3_pr_input].keys()) # Не работает, спросить на уроке
                 print(f'{user_3_pr_input} на складе: {a}')

     # Показ актуальной корзины
     elif user_inp == 4:
             print(f'Ваша корзина: {korz}')

     # Удаление товара из корзины
     elif user_inp == 5:
         print(f'\nВаша корзина: {korz}')
         del_korz = input(f'Выберете товар, который хотите вы хотите удалить из корзины: ').strip().title()
         if del_korz in korz:
             korz.remove(del_korz)
         else:
             print(f'{del_korz} нет в вашей корзине.')

     # Замена товара в корзинке
     elif user_inp == 6:
         print(f'Ваша корзинка: {korz}')
         old_prod = input('Введите товар который вы хотите заменить: ').strip().title()
         new_prod = input('Введите новый товар: ').strip().title()
         new_prod_num = int(input('Какое кол - во вам нужно: '))
         if old_prod in korz :
             a = (new_prod + ' - ' + str(new_prod_num))
             korz.append(a)
             korz.remove(old_prod)

         else:
             print(f'{old_prod} нет на складе.')

















