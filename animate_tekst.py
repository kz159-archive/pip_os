#!/usr/bin/python3
from tkinter import *
import time
import random

COLOR = '#4286f4'
BLOCK = '▇'

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
tekst = c.create_text(400,2500, text = gen_boot(), font = 'monofonto', fill = COLOR)
a = 0
b = -15
for x in range(0 ,300):
    c.move(tekst,a,b)
    gui.update()
    time.sleep(.01)
c.delete(tekst)
gui.title("First title")
canvas_text = c.create_text(50, 50,text="",font = 'monofonto', fill = COLOR, anchor = NW)
test_string = "This is a test"

#Time delay between chars, in milliseconds
delta = 50
delay = 0
for i in range(1,4):
    bleep = c.create_text(50, 50,text=BLOCK,font = 'monofonto', fill = COLOR, anchor = NW)
    gui.update()
    time.sleep(1)
    destroy(bleep)
    gui.update()

for i in range(len(test_string) + 1):
    s = test_string[:i] + BLOCK
    update_text = lambda s=s: c.itemconfigure(canvas_text, text=s)
    c.after(delay, update_text)
    delay += delta
gui.mainloop()
