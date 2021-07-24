credit=int(input('Сколько кредитов вы взяли:'))
if credit<=23:
    print('Студент первокурсник')
elif 24<credit<53:
    print('Студент второкурсник')
elif 54<credit<83:
    print('Студент учится в третьем курсе')
elif 84<credit<120:
    print('Студент выпускник')
