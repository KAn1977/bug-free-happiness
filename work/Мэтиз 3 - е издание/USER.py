class User():
    def __init__(self, first_name, second_name, login, password):
        self.first_name = first_name
        self.second_name = second_name
        self.login = login
        self.password = password

    def describe_user(self):
        print(f'Имя и фамилия пользователя: {self.first_name} {self.second_name}')
        print(f'Логин пользователя: {self.login}')

    def greet_user(self):
        print(f'Hello, {self.login} !')

alan = User('Alan', 'White', 'COOL_AL', 'qwert123')
alan.greet_user()
alan.describe_user()

class Privileges():
    def __init__(self, privileges = ['Разрешенно добавлять сообщения.', 'разрешенно удалять сообщения.',
                                     'Разрешенно банить пользователя.']):
        self.privileges  = privileges

    def show_privileges(self):
        print(f'Все привелегии админа: {self.privileges}')

class Admin(User):
    def __init__(self,first_name, second_name, login, password):
        super().__init__(first_name, second_name, login, password)
        self.ad_privileges = Privileges()



bob = Admin('Bob', 'Martin', 'Bobik','12345')
bob.ad_privileges.show_privileges()
bob.greet_user()