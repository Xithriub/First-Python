import math
def diskrim():
    D=b**2-4*a*c
    print('Дискриминант равен:',D)
    return D
def proverka():
    if   D>0:
        koren2()
    elif D==0:
        koren1()
    elif D<0:
        koren0()
def koren0():
    print('Нет вещественных корней')
def koren1():
    x=-b/(2*a)
    print('Один вещественный корень: х1=х2=',x)
def koren2():
    x1=(-b-math.sqrt(D))/(2*a)
    x2=(-b+math.sqrt(D))/(2*a)
    print('Два вещественных корня: x1=',x1,'x2=',x2)
print('Введите коэффиценты:')
a=float(input('Введите число a:'))
b=float(input('Введите число b:'))
c=float(input('Введите число c:'))
D=diskrim()
proverka()


