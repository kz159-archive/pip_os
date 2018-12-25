#!/usr/bin/python3
from tkinter import *
#from tkinter import messagebox

window = Tk()
C = Canvas(window, bg="blue", height=250, width=300)
file = PhotoImage(file = 'wl.png')
background_label = Label(window, image=file)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

window.mainloop
