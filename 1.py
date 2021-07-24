s=[]
from random import randint
for i in range(100):
    s.append(randint(0,1))
print(s)
n=0
m=0
for j in s:
    if j==0:
        n+=1
    else:
        if m<=n:
            m=n
            n=0
        n=0
print(s)
print('Самое длинный ряд нулей:',m,)

class Wind:
    def __init__(self,plu,min):
        self.plu=plu
        self.min=minus
    def plus_fun(self):
        return self.plu+self.min
    


