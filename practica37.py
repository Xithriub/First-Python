#
#Ученик 8 Б класса Давилов Фархад
def sortirovka(fList):
    fList.sort()
    print('По возрастанию:',*fList)
    fList.reverse()
    print('По убыванию:',*fList)
N=int(input('Сколько чисел вводить?'))
pList=[]
for i in range(N):
    pList.append(int(input('Число:')))
sortirovka(pList)

#
#Ученик 8 Б класса Давилов Фархад
def sravnenieDliny():
    if len(a)>len(b):
        print('Первое число длинее')
    elif len(a)<len(b):
        print('Второе число длинее')
    else:
        print('Числа одинаковой длины')
a=input()
b=input()
sravnenieDliny()

#
#Ученик 8 Б класса Давилов Фархад
def summaTsifr(chislo):
    s=0
    for i in range(len(chislo)):
        s=int(chislo[i])+s
    return(s)
def sravnenieSum():
    if sumA>sumB:
        print('Сумма цифр первого числа больше')
    elif sumA<sumB:
        print('Сума цифр второго числа больше')
    else:
        print('Сума цифр равные')
a=input('Первое число')
b=input('Второе число')
sumA=summaTsifr(a)
sumB=summaTsifr(b)
sravnenieSum()




    