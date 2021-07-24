from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root= Tk()
root.title("БУДИЛЬНИК")
root.geometry("550x350")

mixer.init()

def th():
	t1 = threading.Thread(target=a, args=())
	t1.start()


def a():

	a = h.get()
	if a == "":
		msg = messagebox.showerror('Invalid data','Please enter valid time')
	else:
		Alarmtime= a
		CurrentTime = time.strftime("%H:%M")

		while Alarmtime != CurrentTime:
			CurrentTime = time.strftime("%H:%M")
			
		if Alarmtime == CurrentTime:
			mixer.music.load('bud.mp3')
			mixer.music.play()
			msg = messagebox.showinfo('Пора вставать',f'{am.get()}')
			if msg == 'ok':
				mixer.music.stop()



header =Frame(root)
header.place(x=5,y=5)

hea =Label(root,text="БУДИЛЬНИК",font=('comic sans',20))
hea.pack(fill=X)

panel = Frame(root)
panel.place(x=5,y=70)

alpp = PhotoImage(file='lo.png')

alp = Label(panel,image=alpp)
alp.grid(rowspan=4,column=0)

ati = Label(panel,text="ВРЕМЯ БУДИЛЬНИКА \n(Часы:Минуты)",font=('comic sans',18))
ati.grid(row=0,column=1,padx=10,pady=5)

h = Entry(panel,font=('comic sans',20),width=5)
h.grid(row=0,column=3,padx=10,pady=5)

ame = Label(panel,text="Напишите сообщение",font=('comic sans',20))
ame.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

am = Entry(panel,font=('comic sans',15),width=25)
am.grid(row=2,column=1,columnspan=2,padx=10,pady=5)


st = Button(panel,text="Нажмите на кнопку для того чтобы получить уведомление.",font=('comic sans',20),command=th)
st.grid(row=3,column=1,columnspan=2,padx=10,pady=5)
root.mainloop()

