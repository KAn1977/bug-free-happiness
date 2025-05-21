elif new_prod_input not in all_products['Весь склад']:
print(f'\n{new_prod_input} нет на складе\nХотите добавить этот товар на склад ?\n1 - "Да"\n2 - "Нет"')
choice_6 = int(input('Введите число: '))
if choice_6 == 1:
    all_products['Весь склад'][new_prod_input] = new_prod_num
else:
    print(f'{old_prod_input} нет в корзине.')