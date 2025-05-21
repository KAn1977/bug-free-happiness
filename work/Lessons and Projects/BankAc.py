class BankAc:
    def __init__(self, name, money):
        self.money = money
        self.name = name
        
    def deposit(self,deposit):
        self.money += deposit
        print(f'Депозит равен {deposit}.\n'
              f'Ваш текущий баланс после депозита: {self.money}')

    def cash(self,cash):
        self.money -= cash
        print(self.money)
        
    def balance(self):
        print(f'Текущий баланс: {self.money}')

artur = BankAc('Artur', 10000)

print(f'Данные клиента: {vars(artur)}')
artur.deposit(100)
artur.cash(123)
artur.balance()
