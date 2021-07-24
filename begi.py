


tovar=int(input('Сколько всего товаров?:'))
naimenovanie=[]
tsena=[]
kolvo=[]
itogo=0
for i in range(tovar):
    naimenovanie.append(str(input('Товар:')))
    tsena.append(float(input('Цена:')))
    kolvo.append(float(input('Количество:')))
f=open('Check.txt','w')
print('Наименование', 'Цена(сомов)', 'Количество(шт)', 'Стоимость (сомов)', sep='\t', file=f)
for i in range(tovar):
    print(naimenovanie[i],tsena[i], kolvo[i], tsena[i]*kolvo[i],sep='\t\t', file=f)
    itogo=itogo+tsena[i]*kolvo[i]
print('-'*20,file=f)
print('ИТОГО:',round(itogo,2),'сомов к оплате',file=f)
f.close()
