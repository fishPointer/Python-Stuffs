from tkinter import *

root = Tk()

e = Entry(root, width=64, bg="yellow", fg="black", borderwidth=15)
e.pack()
e.insert(0, "Enter Your Name: ")
# This creates some default text in the box, but won't clear it

def myClick():
    hellostring = "Hello " + e.get()
    myLabel = Label(root, text=hellostring, fg="green")
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()


root.mainloop()
