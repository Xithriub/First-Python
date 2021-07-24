#names={'Fahrum':224,'Alex':335,'Saimon':771,'Diana':112,'Lex':664}
#for k,v in names.items():
    #w=str(input('Введите имя пользователя:'))
    #k=int(input('Введите пароль:'))
    #if w!=k:
        #print('Этот человек является не дейтсвительным пользоваетлем системы')
    #elif w==k:
        #print(v)
#for i,j in names.items():
    #r=str(input('Введите имя пользователя:'))
    #q=int(input('Введите пароль:'))
    #if q!=j:
        #print('Пароль действителен')
    #elif q==j:
        #print('Вы успешно вошли в систему')

s=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
d=dict()
for i in s:
    for j in i:
        if j in d:
            d[j]+=1
        else:
            d[j]-=2
print(d)

    

        


