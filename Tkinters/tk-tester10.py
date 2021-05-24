from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Breadbox GUI')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)



def open():
    top = Toplevel()
    top.title("Anime Girl Central")
    img = PhotoImage(file='/home/eein/Pictures/Anime Girls/1616639527925.png')
    root.call('wm', 'iconphoto', top._w, img)
    lbl = Label(top, text="toplayer").pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()
    pass

btn = Button(root, text="Open new window", command=open).pack()
btn3 = Button(root, text="Exit Program", command=root.quit).pack()

lbl2 = Label(root, text="root layer").pack()



root.mainloop()