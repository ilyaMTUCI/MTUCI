import math

a = int(input('Введите аргумент a: '))
b = int(input('Введите аргумент b: '))
c = int(input('Введите аргумент c: '))
discr = (b**2) - (4*a*c)

if discr>= 0:
    x = (-b + math.sqrt(discr)/(2*a))
    print('Первый корень равен: ', x)
    x = (-b - math.sqrt(discr)/(2*a))
    print('Второй корень равен: ', x)
else:
    print('Дискриминант меньше нуля, корни невещественные')
