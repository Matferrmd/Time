from tkinter import * 
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def clock():
    tick = strftime('%H:%M:%S %p')
    Label.config(text=tick)
    Label.after(1000, clock)

Label = Label(root, font =('ds-digital', 60), background='black', foreground="green")
Label.pack(anchor='center')
clock()
mainloop() 