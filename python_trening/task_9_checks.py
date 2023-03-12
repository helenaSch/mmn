from task_9_oop_1 import*
class Checks:

    def __init__(self, loc):
        self.loc = loc

    def check_text(self, loc):

        search = Input('input#search')
        print(search.loc)
        blue_button = Button('button#blue_button')
        print(blue_button.loc)
        big_title = Title('title#big_title')
        print(big_title.loc)
        blue_link = Link('link#blue_link')
        print(blue_link.loc)
