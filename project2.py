# Калькулятор с использованием модуля Tkinter
from tkinter import *
import math # Импортируем модуль math чтобы обеспечить нашу программу математическими функциями
import parser # Получаем доступ к деревьям синтаксического анализа Python
import tkinter.messagebox # Модуль обеспечивает шаблон для программы

root=Tk()
root.title('Простой Калькулятор') #Название калькулятора
root.configure(background="powder blue")
root.resizable(width=False, height=False)# создаем размер
root.geometry("480x568+0+0")# устанавливаем размер

calc=Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
    # функция для ввода элемента
    def numberEnter(self,num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum=='.':
                if secondnum in firstnum:
                    return
            self.current=firstnum+secondnum
        self.display(self.current)

    # функция для вычисления операции
    def sum_of_total(self):
        self.result=True
        self.current=int(self.current) 
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=int(txtDisplay.get())
            
            


    def display(self,value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="multi":
            self.total*=self.current
        if self.op=="divide":
            self.total /=self.current
        if self.op=="mod":
            self.total %=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
    

    def operation(self,op):
        self.current=int(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
    # функция для удаления элемента
    def Clear_Entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

    # создаем функцию для очистки всего поле ввода
    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0
    
    def mathsPM(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)




    # создаем функцию для периметра
    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)
    # создаем функцию tau
    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)
    
    # создаем функцию для синусов
    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    # создаем функцию е
    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)
    
    # функция для квадрата
    def squared(self):
        self.result=False
        self.current=math.sqrt(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    # создаем функцию для косинусов
    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    # создаем тригонометрическую функцию
    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
    # создаем функцию для тангенсов
    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    # создаем функцию tanh
    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    # создаем функцию sinh
    def sinh(self):
        self.result=False
        self.current=math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    # создаем функцию log
    def log(self):
        self.result=False
        self.current=math.log(float(txtDisplay.get()))
        self.display(self.current)
    # создаем функцию exp
    def exp(self):
        self.result=False
        self.current=math.exp(float(txtDisplay.get()))
        self.display(self.current)
    # Создаем функцию для Возврата обратного гиперболического косинуса числа
    def acosh(self):
        self.result=False
        self.current=math.acosh(float(txtDisplay.get()))
        self.display(self.current)
    # создаем функцию asinh
    def asinh(self):
        self.result=False
        self.current=math.asinh(float(txtDisplay.get()))
        self.display(self.current)
    # создаем функцию expm1
    def expm1(self):
        self.result=False
        self.current=math.expm1(float(txtDisplay.get()))
        self.display(self.current)
    # создаем функцию lgamma
    def lgamma(self):
        self.result=False
        self.current=math.lgamma(float(txtDisplay.get()))
        self.display(self.current)
    # создаем функцию degrees
    def degrees(self):
        self.result=False
        self.current=math.degrees(float(txtDisplay.get()))
        self.display(self.current)
    # создаем функцию log2
    def log2(self):
        self.result=False
        self.current=math.log2(float(txtDisplay.get()))
        self.display(self.current)
    # создаем функцию log10
    def log10(self):
        self.result=False
        self.current=math.log10(float(txtDisplay.get()))
        self.display(self.current)
    # создаем функцию log1p
    def log1p(self):
        self.result=False
        self.current=math.log1p(float(txtDisplay.get()))
        self.display(self.current)




    


added_value=Calc()
txtDisplay=Entry(calc, font=('arial',20,'bold'), bg="powder blue",bd=30, width=29, justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numberpad[i]: added_value.numberEnter(x)
        i+=1 


#==========================Menu==============================#
#Кнопка для очищения 
btnClear=Button(calc,text=chr(67),width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue", command=added_value.Clear_Entry).grid(row=1,column=0,pady=1)
# Кнопка для очищения всего поле ввода
btnAllClear=Button(calc,text=chr(67)+ chr(69),width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue", command=added_value.all_Clear_Entry).grid(row=1,column=1,pady=1)



btnSq=Button(calc,text="/",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.squared).grid(row=1,column=2,pady=1)
# Кнопка для математической функции : +
btnAdd=Button(calc,text="+",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=lambda: added_value.operation("add")).grid(row=1,column=3,pady=1)


# Кнопка для математической функции : -
btnSub=Button(calc,text="-",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=lambda: added_value.operation("sub")).grid(row=2,column=3,pady=1)
# Кнопка для математической функции : *
btnMult=Button(calc,text="*",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=lambda: added_value.operation("multi")).grid(row=3,column=3,pady=1)
btnDiv=Button(calc,text=chr(247),width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=lambda: added_value.operation("divide")).grid(row=4,column=3,pady=1)
                

# кнопка для ввода нуля
btnZero=Button(calc,text="0",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=lambda: added_value.numberEnter(0)).grid(row=5,column=0,pady=1)


# кнопка для ввода точки
btnDot=Button(calc,text=".",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=lambda: added_value.numberEnter(".")).grid(row=5,column=1,pady=1)
btnPM=Button(calc,text=chr(177),width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.mathsPM).grid(row=5,column=2,pady=1)
# Кнопка для вычисления операции
btnEquals=Button(calc,text="=",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue", command= added_value.sum_of_total).grid(row=5,column=3,pady=1)
#==========================Scientific Calculator====================#
# Кнопка для показа числа П
btnPi=Button(calc,text="п",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.pi).grid(row=1,column=4,pady=1)



# Кнопка для вычисления косинуса
btnCos=Button(calc,text="cos",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.cos).grid(row=1,column=5,pady=1)
# Кнопка для вычисления тангенса
btntan=Button(calc,text='tan',width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.tan).grid(row=1,column=6,pady=1)
# Кнопка для вычисления синуса
btnsin=Button(calc,text="sin",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.sin).grid(row=1,column=7,pady=1)


#==================================================================================#
btn2Pi=Button(calc,text="2п",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.tau).grid(row=2,column=4,pady=1)


# кнопка для cosh
btnCosh=Button(calc,text="cosh",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.cosh).grid(row=2,column=5,pady=1)
# кнопка для tahn
btntanh=Button(calc,text='tanh',width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.tanh).grid(row=2,column=6,pady=1)
# кнопка для sinh
btnsinh=Button(calc,text="sinh",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.sinh).grid(row=2,column=7,pady=1)


#==============================================================================================#
# кнопка для log
btnlog=Button(calc,text="log",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.tau).grid(row=3,column=4,pady=1)

# кнопка для Exp
btnExp=Button(calc,text="Exp",width=6,height=2,font=('arial',20,'bold'),bd=4,
                command=added_value.exp).grid(row=3,column=5,pady=1)
# кнопка для mod
btnMod=Button(calc,text='Mod',width=6,height=2,font=('arial',20,'bold'),bd=4,
                command=lambda:added_value.operation).grid(row=3,column=6,pady=1)
# кнопка для е
btnE=Button(calc,text="e",width=6,height=2,font=('arial',20,'bold'),bd=4,
command=added_value.e).grid(row=3,column=7,pady=1)



#=============================================================================================#
# кнопка для log2
btnlog2=Button(calc,text="log2",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.log2).grid(row=4,column=4,pady=1)


# кнопка для deg
btndeg=Button(calc,text="deg",width=6,height=2,font=('arial',20,'bold'),bd=4,
                command=added_value.degrees).grid(row=4,column=5,pady=1)
# кнопка для acosh
btntacosh=Button(calc,text='acosh',width=6,height=2,font=('arial',20,'bold'),bd=4,
                command=added_value.acosh).grid(row=4,column=6,pady=1)
# кнопка для asinh
btnasinh=Button(calc,text="asinh",width=6,height=2,font=('arial',20,'bold'),bd=4,
                command=added_value.sinh).grid(row=4,column=7,pady=1)

#===================================================================================================#
# кнопка для log10
btnlog10=Button(calc,text="log10",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.tau).grid(row=5,column=4,pady=1)

# кнопка для log1p
btnCos=Button(calc,text="log1p",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.cos).grid(row=5,column=5,pady=1)
# кнопка для expm1
btnexpm1=Button(calc,text='expm1',width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.expm1).grid(row=5,column=6,pady=1)
# кнопка для lgamma
btnlgamma=Button(calc,text="lgamma",width=6,height=2,font=('arial',20,'bold'),bd=4,
                bg="powder blue",command=added_value.lgamma).grid(row=5,column=7,pady=1)


lblDisplay=Label(calc, text="Калькулятор",font=('arial',30,'bold'), justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)
#==========================Menu and function=================#
def iExit(): # создаем функцию выхода
    iExit=tkinter.messagebox.askyesno("Простой калькулятор","Вы хотите выйти из приложения?")
    if iExit > 0:
        root.destroy()
        return 


def Scientific():
    root.resizable(width=False, height=False)# создаем размер
    root.geometry("944x568+0+0")# устанавливаем размер


def Standard():
    root.resizable(width=False, height=False)# создаем размер
    root.geometry("480x568+0+0")# устанавливаем размер



# создаем меню
menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="File", menu=filemenu)# создаем вкладку File
filemenu.add_command(label="Обычный", command=Standard)# создаем вкладку Обычный калькулятор
filemenu.add_command(label="Научный калькулятор", command=Scientific)# создаем вкладку научный калькулятор
filemenu.add_separator()
filemenu.add_command(label="Exit",command=iExit)# создаем вкладку для выхода из приложения

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Edit", menu=editmenu)
filemenu.add_command(label="Cut")
filemenu.add_command(label="Copy")
filemenu.add_separator()
filemenu.add_command(label="Paste")

helpmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=editmenu)
editmenu.add_command(label="View Help!")

root.config(menu=menubar)
root.mainloop()




