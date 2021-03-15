#Here we can create our project

from tkinter import *

window = Tk()

window.title("Welcome to our prject")

window.geometry('350x200')

lbl = Label(window, text="NASA")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click if you feel chalinga!")

btn.grid(column=1, row=0)

window.mainloop()