class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def show_my_drink(self):
        if self.taste:
            print(f'У газировки {self.taste}')
        else:
            print('Обычная газировка')

strawberry_taste = Soda('клубничный вкус')
simple_taste = Soda()

strawberry_taste.show_my_drink()
simple_taste.show_my_drink()