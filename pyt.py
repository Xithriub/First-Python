#def function(a,b):
    #return (a+b)**2
#a=int(input('Введиет число:'))
#b=int(input('Введите число:'))
#print(function(a,b)

import random
q=[]
w=random.randint(-100,100)
Nul=0
Plus=0
otric=0
for i in range(w):
    if i==0:
        Nul+=0
    elif i>0:
        Plus+=1
    elif i<0:
        otric+=1
print('Числа равные нулю:',Nul)
print('Положительные числа:',Plus)
print('Отрицательные числа:',otric)

