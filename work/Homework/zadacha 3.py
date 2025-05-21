class Math:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def addition(self):
        sum  = self.a + self.b
        print(f'Сумма чисел {self.a} и {self.b} равна {sum}')

    def multiplication(self):
        mult = self.a * self.b
        print(f'Произведение чисел {self.a} и {self.b} равна {mult}')

    def substraction(self):
        sub = self.a - self.b
        print(f'Вычитание чисел {self.a} и {self.b} равна {sub}')

    def division(self):
        if self.b != 0:
            div = self.a / self.b
            print(f'Вычитание чисел {self.a} и {self.b} равна {div}')
        else:
            print('Делить на ноль нельзя.')

nums = Math(7, 0)
nums.addition()
nums.multiplication()
nums.substraction()
nums.division()

