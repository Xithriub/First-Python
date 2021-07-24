def plus(a,b):
    return a,b
def minus(a,b):
    return a,b
def delenie(a,b):
    return a,b
def umnozhenie(a,b):
    return a,b
x=int(input('Введите x: '))
y=int(input('Введите y: '))
znak=str(input('Введите знак операции: + - / *' +'\n'))
print('Ответ:',end='')
if znak=='+':
    print(plus(x,y))
elif znak=='-':
    print(minus(x,y))
elif znak=='/':
    print(delenie(x,y))
elif znak=='*':
    print(umnozhenie(x,y))
    

