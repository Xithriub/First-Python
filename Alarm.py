from tkinter import *
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox
root=Tk()
root.title("Alarm Clock")
root.geometry("660x330")
alarmtime=StringVar()
msgi=StringVar()
head=Label(root,text="Alarm Clock",font=('comic sans',20))
head.grid(row=0,columnspan=3,pady=10)
mixer.init()

def alarm():
    a=alarmtime.get()
    Alaram=a
    currenttime=time.strftime("%H:%M")
    while Alaram!=currenttime:
        currenttime=time.strftime("%H:%M")
    if Alaram==currenttime:
        mixer.music.load('zvuk.mp3')
        mixer.music.play()
        msg=messagebox.showinfo('Info',f'{msgi.get()}')
        if msg=='ok':
            mixer.music.stop()


Clockimg=PhotoImage(file="Cl.png")

img=Label(root,image=Clockimg)
img.grid(rowspan=4,column=0)
inputt=Label(root,text='Input time',font=('comic sans',15))
inputt.grid(row=1,column=1)

alttime=Entry(root,textvariable=alarmtime,font=('comic sans',18),width=6)
alttime.grid(row=1,column=2)

msg=Label(root,text="Message",font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=2)

msginput=Entry(root,textvariable=msgi,font=('comic sans',18))
msginput.grid(row=3,column=1,columnspan=2)

sub=Button(root,text="Submit",font=('comic sans',18))
sub.grid(row=4,column=1,columnspan=2)

root.mainloop()