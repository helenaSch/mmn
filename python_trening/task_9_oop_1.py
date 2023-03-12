from task_9_checks import Checks
class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search = Input('input#search', 'find me')
print(search.loc)
print(search.text)

class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

blue_button = Button('button#blue_button', 'Tap me')
print(blue_button.loc)
print(blue_button.text)


class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


big_title = Title('title#big_title', 'Something')
print(big_title.loc)
print(big_title.text)

class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


blue_link = Link('link#blue_link', 'where this link')
print(blue_link.loc)
print(blue_link.text)


