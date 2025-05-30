# Задания для повторения материала (Мэтиз, главы 1-9)

"""
Каждое задание построено таким образом, чтобы охватить несколько концепций из разных глав.
Рекомендуется выполнять задания по порядку, так как они могут использовать знания из предыдущих заданий.
"""

# Задание 1: Обработка информации о пользователях (Глава 2)
"""
Создайте программу для обработки данных пользователей.

Требования:
1. Создайте функцию format_user_data(first_name, last_name, age, email)
2. Функция должна:
   - Привести имя и фамилию к правильному формату (первая буква заглавная, остальные строчные)
   - Проверить корректность email (привести к нижнему регистру)
   - Создать строку с информацией о пользователе
   - Добавить проверку возраста (должен быть в диапазоне 0-120)
3. Создайте функцию calculate_statistics(numbers), которая принимает список чисел и возвращает словарь
   со следующими расчетами:
   - среднее значение
   - сумма
   - произведение
   - разница между максимальным и минимальным значением
"""
first_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
email = input('Введите вашу электронную почту: ')

while True:
    try:
        age = int(input('Введите ваш возраст: '))
        break
    except ValueError:
        print('Введите число.')

def format_user_data():
    print(first_name.title())
    print(last_name.title())
    print(email.lower())
    if age in range(0, 121):
        print(age)
    else:
            pass
format_user_data()
# Задание 2: Управление списком задач (Главы 3-4)
"""
Создайте систему управления задачами.

Требования к классу TaskManager:
1. Хранение задач в списке с приоритетами
2. Методы:
   - add_task(task, priority) - добавление задачи с приоритетом
   - remove_task(task) - удаление задачи
   - get_sorted_tasks() - получение отсортированного списка задач
   - get_high_priority_tasks() - получение только важных задач
3. Каждая задача должна хранить:
   - название
   - приоритет (высокий, средний, низкий)
   - дату создания
   - статус (новая, в процессе, завершена)
"""

# Задание 3: Игра "Угадай число" (Глава 5)
"""
Создайте игру, где компьютер загадывает число, а игрок должен его угадать.

Требования к классу NumberGame:
1. Инициализация с диапазоном чисел (min_num, max_num)
2. Методы:
   - make_guess(number) - проверяет предположение игрока и возвращает подсказки:
     * "Горячо!" - если разница не более 5
     * "Тепло" - если разница не более 10
     * "Холодно" - в остальных случаях
     * Дополнительно: "больше" или "меньше"
3. Подсчет количества попыток
4. Возможность начать новую игру
"""

# Задание 4: Система управления инвентарем (Глава 6)
"""
Создайте систему для управления складским инвентарем.

Требования к классу InventorySystem:
1. Хранение информации о товарах в словаре
2. Методы:
   - add_item(item_name, quantity, price, category)
   - remove_item(item_name, quantity)
   - get_category_items(category)
   - get_total_value()
3. Каждый товар должен содержать:
   - название
   - количество
   - цену
   - категорию
4. Реализуйте подсчет общей стоимости инвентаря
"""

# Задание 5: Система опроса пользователей (Глава 7)
"""
Создайте систему для проведения опросов.

Требования к классу SurveySystem:
1. Методы:
   - run_survey() - запуск опроса пользователей
   - get_statistics() - получение статистики по ответам
2. Функционал:
   - Непрерывный опрос пользователей до команды выхода
   - Сохранение всех ответов
   - Возможность просмотра статистики
3. Каждый опрос должен содержать минимум 3 вопроса
4. Реализуйте анализ популярных ответов
"""

# Задание 6: Текстовый анализатор (Глава 8)
"""
Создайте инструмент для анализа текста.

Требования:
1. Функция text_analyzer(text) должна возвращать словарь со статистикой:
   - количество слов
   - количество предложений
   - самое длинное слово
   - самое часто встречающееся слово
   - средняя длина слова
2. Функция format_text(*paragraphs, width=80, alignment='left'):
   - форматирование текста с заданной шириной
   - поддержка выравнивания (по левому краю, правому краю, по центру)
   - работа с несколькими параграфами
"""

# Задание 7: Библиотечная система (Глава 9)
"""
Создайте систему управления библиотекой.

Требования:
1. Классы:
   - Book (название, автор, ISBN, год, жанр)
   - Member (имя, ID читателя)
   - Library (управление книгами и читателями)

2. Методы класса Library:
   - add_book(book)
   - register_member(member)
   - loan_book(book, member)
   - return_book(book, member)
   - get_member_books(member)
   - get_available_books()
   - search_books(**kwargs)

3. Функционал:
   - Учет доступных книг
   - Регистрация читателей
   - Выдача и возврат книг
   - Поиск книг по различным критериям
   - Отслеживание сроков возврата

4. Создайте тестовую функцию test_library_system() для проверки всей функциональности
"""

if __name__ == "__main__":
    print("Выберите задание для выполнения (1-7):")
    print("1. Обработка информации о пользователях")
    print("2. Управление списком задач")
    print("3. Игра 'Угадай число'")
    print("4. Система управления инвентарем")
    print("5. Система опроса пользователей")
    print("6. Текстовый анализатор")
    print("7. Библиотечная система")
