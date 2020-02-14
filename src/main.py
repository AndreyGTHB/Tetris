from tkinter import *
from time import sleep
from random import choice

window = Tk()
window.title("Tetris")


WIDTH = 550
HEIGHT = 600
c = Canvas(window, width=WIDTH, height=HEIGHT)
c.pack()

background = c.create_rectangle(0, 0, WIDTH, HEIGHT, fill="lightblue")

tile_size = 50

window.mainloop()



