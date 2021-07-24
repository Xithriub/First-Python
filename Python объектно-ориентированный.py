# class Person:
# def __init__(self,name,fam,ot,godRojd):
# self.imya=name
# self.fam=fam
# self.otchestvo=ot
# self.vozr=2021-godRojd
# def fio(self):
# return self.fam+' '+self.imya
# def godRojdeniya(self):
# return self.vozr
# def __str__(self):
# return self.fam+' '+self.imya+' '+self.otchestvo
# b=Person('Burul','Shambetova','Shambetovna',2000)
# print(b)
# print(b.fio())
# print(b.godRojdeniya())
# q=Person('Fatima','Zhylbek','Zhyldyzbek',2008)
# print(q.fio())


# class Product:
# def __init__(self,name,amount,price):
# self.name=name
# self.amount=amount
# self.price=price
# def get_price(self,want):
# n=want
# if n>=1 and n<10:
# return self.price
# elif n>=10 and n<=99:
# return self.price - (self.price * 0.1)
# elif n>=100:
# return self.price - (self.price * 0.2)
# def make_purchase(self,n):
#self.amount -=n
# return self.amount
#class Password_manager:
    #def __init__(self):
        #self.old_passwords=['hii','heloo','23232']
    #def get_password(self):
        #return self.old_password[-1]
    #def set_password(self,passowrd):
        #if passowrd not in self.old_passwords:
            #self.old_passwords.append(passowrd)
    #def is_correct(self,parol):
        #return parol==self.old_passwords[-1]
 #gmail=Password_manager()
 #print(gmail.get_password())
 #gmail.get_password('Asfeg')
 #print(gmail.get_password())
 #print(gmail.is_correct('12345678'))

# 4
# class Time:
# def __init__(self,sek,):
# self.sek=sek
# def convert_to_minutes(self):
# minutes=self.sek//60
# r=self.sek%60
# return '():()'.format(minutes,r)
# def convert_to_hours(self):
# rem=self.sek%60
# minutes=self.sek//60
# m=minutes%60
# hours=minutes//60
# return '():():()'.format(hours,m,rem)
# wert=Time(3675)
# print(wert.convert_to_minutes())
# print(wert.convert_to_hours())
# 5

# class Wordplay:
# def __init__(self):
# self.names=['Fas','Rainbow','Savage','rider',Saiyu','someone','Lion','Father']
# def words_with_length(self,typ):
# self.typ=typ
# self.typ=typ
# for i in

#class Converter:
#for i in range(1,6):
    #for j in range(1,6):
        #if (i==3)or(j==3):
            #print('#',end='')
        #else:
            #print('o',end='')
    #print()
def proverka():
    a=40
    b=60
    c=a+b
    return(c)
k=10
m=20
n=k+m
print('k+m=',n)
