from cgitb import text
from tkinter import *

root = Tk()
root.title("Hello World")
def button_add():
    return

buttons = []
for i in range(9):
    buttons.append(Button(root, text=i, padx=40, pady=20, command=button_add))

e = Entry(root, width=20, borderwidth=5)
e.grid(row = 0, column=0, columnspan=3, padx=10, pady=10)
col = 0
for index, button in enumerate(buttons):
    button.grid(row=index%3,column=col)
    if index%3 == 1:
        col = 1
    elif index%3 == 2:
        col =2

e.insert(0, "Enter Your Name")
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
mybutton = Button(root, text='Enter Your Stock Quote', command=myClick)

root.mainloop()