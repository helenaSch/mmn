from task_9_checks import Check
class Input(Check):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search = Input('input#search', 'find me')
print(search.loc, search.text)
print(search.check_text())

class Button(Check):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

blue_button = Button('button#blue_button', 'Tap me')
print(blue_button.loc, blue_button.text)
print(blue_button.check_text())


class Title(Check):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


big_title = Title('title#big_title', 'Something')
print(big_title.loc, big_title.text)
print(big_title.check_text())


class Link(Check):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


blue_link = Link('link#blue_link', 'where this link')
print(blue_link.loc, blue_link.text)
print(blue_link.check_text())


