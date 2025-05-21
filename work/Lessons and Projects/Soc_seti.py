class Soc_s:
    def __init__(self, name, mail, age, number):
        self.name = name
        self.mail = mail
        self.age = age
        self.number = number

    def change_name(self,new_name):
        self.name = new_name
        print(f'Ваш старый никнейм {self.name} заменен на новый - {new_name}')

    def change_age(self,new_age):
        self.age = new_age
        print(f'Ваш старый возраст {self.age} заменен на новый - {new_age}')

    def change_number(self,new_number):