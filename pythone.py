#def Skruga(radius):
    #return pi*(radius**2)
#pi=3.14
#r=float(input('Введите радиус круга:'))
#print('Функция s=',Skruga(r))
#print('Лямбда-ф s=',(lambda radius: pi*(radius**2))(r))

#def V(a,b,h):
    #return a*b*h
#a=float(input('Введите длину:'))
#b=float(input('Введите ширину:'))
#h=float(input('Введите высоту:'))
#print('Функция V= ',V(a,b,h))
#LambdaV=lambda  a,b,h: a*b*h
#print('Лямбда V=',LambdaV(a,b,h))

def unical_function(b):
    q=[]
    for i in range(b):
        if i%2==0:
            q.append(i)
    return q
b=int(input('Введите число:'))
print(unical_function(b))


vvod=str(input('Введите слово:'))
q=[]
for i in range(len(vvod)):
    if 'a' or 'i' or 'e' in vvod:
        q.append(vvod)
print(q)

class Time:
    def __init__(self,sec):
        self.sec=sec
    def convert_to_minutes(self):
        minuts=sel.sec//60
        rem=

