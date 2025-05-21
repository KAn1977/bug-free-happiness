class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('\nАвтомобиль заведен.')

    def off(self):
        print('\nАвтомобиль заглушен.')

    def new_year(self, new_year):
        self.year = new_year
        print(f'\n{new_year} - Новый год выпуска машины.')

    def new_type(self, new_type):
        self.type = new_type
        print(f'\n{new_type} - новый тип автомобиля.')

    def new_color(self, new_color):
        self.color = new_color
        print(f'\n{new_color} - новый цвет автомобиля.')

lada = Car('green', 'picap', 2000)

lada.start()
lada.off()
lada.new_year(2000)
lada.new_type('cabriolet')
lada.new_color('red')

