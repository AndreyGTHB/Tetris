from tkinter import *
from threading import Timer

root = Tk()


def printer(event):
    print("Hello World again!")


c = Canvas(root, width=500, height=500)
c.pack()

shape = c.create_oval(10, 10, 110, 110, fill="blue")
def change_shape():
    global shape
    c.itemconfig(shape, fill="green")

t = Timer(2, change_shape)
t.start()

root.mainloop()
