#Площадь круга
#Ученик 8 Б класса Давилов Фархад
def Skruga(radius):
    return pi*(radius**2)
pi=3.14
r=float(input('Введите радиус круга:'))
print('Функция s=',Skruga(r))
print('Лямбда-ф s=',(lambda radius: pi*(radius**2))(r))

#Объем параллелепипеда
#Ученик 8 Б класса Давилов Фархад
def V(a,b,h):
    return a*b*h
a=float(input('Введите длину:'))
b=float(input('Введите ширину:'))
h=float(input('Введите высоту:'))
print('Функция V= ',V(a,b,h))
LambdaV=lambda  a,b,h: a*b*h
print('Лямбда V=',LambdaV(a,b,h))





