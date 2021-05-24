from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Breadbox GUI')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)
root.geometry("400x400")

def show():
    lbl = Label(root, text=var.get()).pack()

optionslist = [
    "Monday",
    "Tuesday", 
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

var = StringVar()
var.set("Monday")

drop = OptionMenu(root, var, *optionslist) #you need the star up front
drop.pack()

btn = Button(root, text="Show Selection", command=show).pack()



root.mainloop()
