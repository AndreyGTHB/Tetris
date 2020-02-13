from tkinter import *
from time import sleep
from random import choice

window = Tk()
window.title("Tetris")


width = 550
height = 600
c = Canvas(window, width=width, height=height)
c.pack()

background = c.create_rectangle(0, 0, width, height, fill="blue")


