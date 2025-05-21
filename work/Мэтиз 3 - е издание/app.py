class Car:
    def __init__(self, brand, year, model):
        # Приватные атрибуты
        self.__mileage = 0
        # Защищенные атрибуты
        self._brand = brand
        self._year = year
        # Публичный атрибут
        self.model = model

    # Публичный метод
    def get_mileage(self):
        return self.__mileage

    # Защищенный метод
    def _update_mileage(self, miles):
        if miles > 0:
            self.__mileage += miles

    # Приватный метод
    def __service_check(self):
        return self.__mileage > 10000

aa = Car('toyota', 2024, 's')
aa.