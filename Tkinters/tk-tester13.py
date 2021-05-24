from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Breadbox GUI')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)
root.geometry("400x400")

def update():
    lbl = Label(root, text=var.get()).pack()

var = IntVar()  

chk = Checkbutton(root, text="don't click this", variable=var, onvalue=2, offvalue=6).pack()

btn = Button(root, text="Show Selection", command=update).pack()


root.mainloop()

