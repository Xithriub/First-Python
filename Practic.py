from random import randint
doll=100
rand=randint(1,2)
while doll!=rand:
    print(rand)
    guess=int(input('Введите число:'))
    if guess==rand:
        doll+=9
    elif guess!=rand:
        doll-=10
    elif doll==200:
        print('Игра окончена')


    
