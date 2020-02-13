from tkinter import *

root = Tk()


def printer(event):
    print("Hello World again!")


class OrderPage:
    def __init__(self):
        self.label1 = Label(root,
                            width=30,
                            text="Ваш e-mail:",
                            font="Arial 18"
                            )
        self.label2 = Label(root,
                            width=30,
                            text="Комментарий к заказу:",
                            font="Arial 18"
                            )
        self.field1 = Entry(root,
                            width=23,
                            bd=3
                            )
        self.field2 = Text(root,
                           font="Verdana 12",
                           wrap=WORD
                           )
        self.but = Button(root,
                          text="OK"
                          )

        self.but.bind("<Button-1>", self.info)
        self.but.pack()

        self.label1.pack()
        self.field1.pack()

        self.label2.pack()
        self.field2.pack()

    def info(self, event):
        print("Email for info: " + self.field1.get())
        print("Comment for order: " + self.field2.get(1.0, END))


order = OrderPage()
root.mainloop()
