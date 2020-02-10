from tkinter import *
from time import sleep

window = Tk()
window.title("Tetris")


width = 550
height = 600
c = Canvas(window, width=width, height=height)
c.pack()

background = c.create_rectangle(0, 0, width, height, fill="blue")

window.mainloop()