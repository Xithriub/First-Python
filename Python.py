#items=[1,2,3,4,5,6,7,8,9,10]

#num=int(input())
#items[num]='x'
#print(items)

#words=['Python','fun']
#index=1
#words.insert(index,'is')
#print(words)

#nums=[9,8,7,6,5]
#nums.append(4)
#nums.insert(2,11)
#print(nums)

# letters=['p','q','r','s','p','u','p']
# print(letters.index('r'))
# print(letters.index('p'))
# print(max(letters))
# print(min(letters))
# print(letters.count('p'))

# numbers=[14,5,6,8,17,28]
# mon=min(numbers)+max(numbers)
# print(mon)


# queue=['John','James','Amy']
# txt=input()
# queue.append(txt)
# print(queue)

# items=[2,4,6,8,10,12,14]
# print(len(items)//2)

# i=3
# while i>=0:
#     print(i)
#     i=i-1
# print('Finished')


# x=1
# while x<10:
#     if x%2==0:
#         print(str(x)+"is even")
#     else:
#         print(str(x)+"is odd")
#     x+=1

# x=0
# while x<=20:
#     print(x)
#     x+=2

# i=0
# while True:
#     print(i)
#     i=i+1
#     if i>=5:
#         print('Breaking')
#         break

# print('Finished')


# i=1
# while i<=5:
#     print(i)
#     i+=1
#     if i==3:
#         print('Skipping 3')
#         continue

# items=[23,555,666,123,128,4242,990]
# sum=0
# n=0
# while n<len(items):
#     num=items[n]
#     n+=1
#     if num%2!=0:
#         continue
#     sum+=num

# print(sum)

# items=[]

# while True:
#     n=int(input())
#     if n==0:
#         break
#     items.append(n)

# print(items)

# n=int(input())
# length=0
# while n>0:
#     n//=10
#     length+=n%10
#     length+=2
    
# print(length)

import turtle
colors=['red','purple','blue','green','yellow','orange']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])  
    t.width(x/100+1)
    t.forward(x)
    t.left(59)  
    