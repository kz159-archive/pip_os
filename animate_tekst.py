#!/usr/bin/python3
from tkinter import *
import time
import random

gui = Tk()
var=IntVar()
gui.geometry("800x800")
c = Canvas(gui ,width=800 ,height=800)
photo = PhotoImage(file = "wl.png")
c.pack()

def gen_boot():

    ENDS = ['A4', '14', '3D', '9']
    STARTS = ['CPU0 launch EFI0', 'start memory discovery', 'CPU0 start cell relocation']
    line = (
    '{} 0 0x0000A4 0x0000000000000000 1 0 0x000014 \n'
    '0x0000000000000000 {} 0 0x0000A4\n'
    '0x0000000000000000 1 0 0x000009 0x0000000000000000 {}\n'
    '0x0000A4 0x0000000000000000 1 0 0x000009 0x0000000000000000E003D\n'
    '{} 0x0000A4 0x0000000000000000 1 0 0x0000A4\n'
    '0x0000000000000000 {}0 0x0000A4 0x0000000000000000\n'
    '1 0 0x0000A4 0x0000000000000000 {} 0 0x0000A4\n'
    '0x0000000000000000 1 0 0x000014 0x0000000000000000 {}\n'
    '0x0000000000000000 {}0 0x0000A4 0x0000000000000000000000000E003D\n'
    ).format(random.choice(STARTS), random.choice(STARTS), random.choice(STARTS), random.choice(STARTS), random.choice(STARTS), random.choice(STARTS), random.choice(STARTS), random.choice(STARTS))
    line += line*11
    return line

#oval = c.create_oval(5,5,60,60,fill='pink')
imagesprite = c.create_image(400,400,image=photo)
tekst = c.create_text(400,2500, text = gen_boot(), font = 'monofonto', fill = '#4286f4')
a = 0
b = -15
for x in range(0 ,1000):
    c.move(tekst,a,b)
    gui.update()
    time.sleep(.01)
gui.title("First title")
gui.mainloop()
