class Comment:
    def __init__(self, username, text, likes):
        self.username = username
        self.text = text
        self.likes = likes

    def block(self):
        print('Заблокировать')

    def change_likes(self, reaction):
        self.likes = reaction

artur = Comment('Killa', 'Hahahaha',1)
artur.block()
artur.change_likes('Good')
print(vars(artur))
