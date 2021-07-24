vsego=int(input('Сколько чисел ввести?:'))
spisok=[]
import random
for i in range(vsego):
    spisok.append(random.randint(-10,10))
    print(spisok[i])
kolvoPolozh=kolvoOtric=kolvoNul=0
for i in range(vsego):
    if spisok[i]==0:
        kolvoNul+=1
    elif spisok[i]>0:
         kolvoPolozh+=1
    elif spisok[i]<0:
        kolvoOtric+=1
print('Положительных:',kolvoPolozh)
print('Отрицательных:',kolvoOtric)
print('Нулей:',kolvoNul)
