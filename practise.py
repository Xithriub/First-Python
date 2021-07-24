#vvod=str(input('Введите строку:'))
#print(vvod[:5])
#print(vvod[5:7])

#bukvy='abcdefghijklmnopqrstuvwxy'
#for i in range(26):
    #print(bukvy[i:]+bukvy[:i])
def celsius_to_fahrenheit(x):
    return(9/5)*(x+32)
def fahrenheit_to_celsius(x):
    return(5/9)*(x-32)
temp=float(input('Введите число:'))
c=input('F(ahrenheit) or C(elsius):')
if c=='F' or c=='f':
    x=fahrenheit_to_celsius(temp)
    print(temp,'C=',x,'F')
else:
    x=celsius_to_fahrenheit(temp)
    print(temp,'F=',x,'C')

        

            
    
