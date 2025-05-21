class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant is open')

    def name(self):
        long_name = f'{self.restaurant_name} {self.cuisine_type}'
        print(long_name)
        return long_name

    def new_num_served(self,cl):
        if cl >= self.number_served:
            self.number_served = cl
            print(self.number_served)
        else:
            print('Кол - во обслуженных клиентов не может уменьшиться.')

    def add_number_served(self,new_cl):
        self.number_served += new_cl
        print(self.number_served)


Waka = Restaurant('Waka', 'korean')
Waka.new_num_served(213123)
Waka.add_number_served(123123)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def check_flavors(self):
        print(f'Сорт мороженного: {self.flovors}')












