def Skruga(radius):
    return pi*(radius**2)
pi=3.14
r=float(input('Введите радиус круга:'))
print('Функция s=',Skruga(r))
print('Лямбда-ф s=',(lambda radius: pi(radius**2))(r))
