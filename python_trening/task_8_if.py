num = -9
if num >= 0:
    print('Число больше или равно нулю')
else:
    print('Число отрицательное')


# str2 содержит в себе str1?

str1 = 'test'
str2 = 'test1'
if (str1 in str2):
    print("Yes")
else:
    print("No")

num_float = -9

if num_float >0:
    print('Положительное число')
elif num_float ==0:
    print('Ноль')
else:
    print('Отрицательное число')

num = 8
permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

age = 11
if age >=1 and age <=4:
    print('Бакалавр')
elif age >=5 and age <=6:
    print('Магистр')
elif age >= 8 and age <= 9:
    print('Аспирант')
else:
    print('Введите корректный год обучения.')

a = 1
if a in range (1,4):
    print('Бакалавр')
elif a in range (5,6):
    print('Магистр')
elif a in range (7,9):
    print('Аспирант')
else:
    print('Введите корректный год обучения.')
