#!/usr/bin/env python3
# -*-coding: utf8-*-
from tkinter import *
root = Tk()
photo = PhotoImage(file = "wl.png")
w = Label(root, image=photo)
w.pack()
#ent = Entry(root)
#ent.pack()
#ent.focus_set()
text = Text(width=25, height=5, bg="darkgreen", fg='white', wrap=WORD)
text.pack()
root.config(cursor = 'none')
root.mainloop()
