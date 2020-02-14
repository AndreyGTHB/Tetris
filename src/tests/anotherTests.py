from tkinter import *

root = Tk()


def printer(event):
    print("Hello World again!")


def test_range():
    list = [1, 2, 3, 4]
    for i in range(len(list)):
        print(list[i])

test_range()


