from tkinter import *


root = Tk()

def myClick():
    myLabel = Label(root, text="Look, I clicked a Button!", fg="green")
    myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()


root.mainloop()
