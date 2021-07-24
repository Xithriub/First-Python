from tkinter import *
import math as M

root=Tk()
root.title('Простой Калькулятор')
e=Entry(root,width=50,borderwidth=5,relief=RIDGE,fg="White",bg="Black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)


def click(to_print):
    old=e.get()
    e.delete(0, END)
    e.insert(0, old+to_print)
    return

def sc(event):
    key=event.widget
    text=key['text']
    no=e.get()
    result=''
    if text=='deg':
        result=str(m.degrees(float(no)))
    if text=='sin':
        result=str(m.sin(float(no)))
    if text=='cos':
        result=str(m.sin(float(no)))
    if text=='tan':
        result=str(m.tan(float(no)))
    if text=='lg':
        result=str(m.log10(float(no)))
    if text=='ln':
        result=str(m.log(float(no)))
    if text=='Sqrt':
        result=str(m.sqrt(float(no)))
    if text=='x!':
        result=str(m.factorial(float(no)))
    if text=='1/x':
        result=str(1/(float(no)))
    if text=='pi':
        if no=="":
            result=str(m.pi)
        else:
            result=str(float(no)*m.pi)
    if text=='e':
        if no=="":
            result=str(m.e)
        else:
            result=str(m.e**float(no))
    e.delete(0, END)
    e.insert(0, result)

def clear():
    e.delete(0, END)
    return

def bksps():
    current=e.get()
    length=len(current)-1
    e.delete(length, END)

def evaluate():
    ans=e.get
    ans=eval(ans)
    e.delete(0, END)
    e.insert(0, ans)


lg=Button(root, text="lg", padx=28, pady=28, pady=10,relief=RIDGE)
lg.bind("<Button-1>", sc)
ln= Button(root, text="ln", padx=28, pady=10,relief=RIDGE)





