from tkinter import *



window = Tk()
window.title("Tetris")

width = 550
height = 650
c = Canvas(window, width=width, height=height)
c.pack()
background = c.create_rectangle(0, 0, width, height, fill = "blue")






