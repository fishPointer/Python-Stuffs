from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Breadbox GUI')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)


def open():
    global imgg
    root.filename = filedialog.askopenfilename(initialdir="/home/eein/Pictures/Anime Girls", title="Select a girl", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    lbl = Label(root, text=root.filename).pack()
    imgg = ImageTk.PhotoImage(Image.open(root.filename))
    imgglbl = Label(image=imgg).pack()


root.title('Breadbox GUI')
root.mainloop()