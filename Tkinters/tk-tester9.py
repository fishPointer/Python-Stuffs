from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Breadbox GUI')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)


#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("Titlebar", "Hello World")
    Label(root, text=response).pack()


Button(root, text="popup", command=popup).pack()



root.mainloop()
