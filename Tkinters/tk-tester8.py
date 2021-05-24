from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Radio Button Tutorial')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)

#r = IntVar() #allows kinter to track variable, but you have to call r.get() to retrieve it
# not a regular python variable. StrVar() is also an option
#r.set() is also an option


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),

]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode, command=lambda: clicked(pizza.get())).pack(anchor=W)


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="Click me", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()