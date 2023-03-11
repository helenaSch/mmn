a = 9
b = 15
def task_1(a, b):
    return a or b
if a > b:
    print(a)
else:
    print(b)


d = 500
c = 365
def task_2(d, c):
    return 
if d - c == 135 or c - d == 135:
    print('Yes')
else:
    print('No')


month = 3
def task_3(month):
    return
if month == 1 or month == 2 or month == 12:
    print('Зима')
elif month == 3 or month == 4 or month == 5:
    print('Весна')
elif month == 6 or month == 7 or month == 8:
    print('Лето')
elif month == 9 or month == 10 or month == 11:
    print('Осень')
else:
    print('Boo!') 


k, n, l = 5, 16, 17
def task_5(k, n, l):
    return
if k > 10 and n > 10 and l > 10:
    print('Yes')
else:
    print('No')


def task_3(my_list):
    counter = 0
    for any_element in my_list:
        if any_element >0:
            counter += 1
    return counter
print(task_3([6, 7, -8, 9, 3]))


def numbers_of_days(month, years):
    return (29 * month) * years
result = numbers_of_days(12, 6)
print(result)


