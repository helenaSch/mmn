class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 *(self.width + self.length)

first = Rectangle(5, 7)
second = Rectangle(8, 9)
third = Rectangle(2, 3)
print('Площадь 1:', first.area())
print('Площадь 2:', second.area())
print('Площадь 3:', third.area())
print('Периметр 1:', first.perimeter())
print('Периметр 2:', second.perimeter())
print('Периметр 3:', third.perimeter())


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)



class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

    def click(self):
        return "Клик по кнопке {}".format(self.text)
    
text_box = Button('Text Box', '')
check_box = Button('Check Box', '')
radio_button = Button('Radio Button', '')
web_tables = Button('Web Tables', '')
buttons = Button('Buttons', '')
links = Button('Links', '')
broken_links_images = Button('Broken Links - Images', '')
upload_and_download = Button('Upload and Download', '')
dynamic_properties = Button('Dynamic Properties', '')

print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(broken_links_images.click())
print(upload_and_download.click())
print(dynamic_properties.click())








