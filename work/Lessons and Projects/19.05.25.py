class Animal:
    def make_sound(self, s):
        print(s)

class Horse(Animal):
    pass


pony = Horse()



class Roditel:
    def __init__(self,color,eye):
        self.color = color
        self.eye = eye

    def krik(self):
        print('AAAAAAAAAAA')



class Rebenok(Roditel):
    pass

bob = Rebenok('white','brown')

bob.krik()


class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year



class SuperCar(Car):
    def __init__(self, model, color, year, sponsor):
        super().__init__(model, color, year)
        self.sponsor = sponsor
