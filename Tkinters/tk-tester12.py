from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Breadbox GUI')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)

def update():
    resstring = (str(horizontal.get()) + "x" + str(vertical.get()))
    dimlbl = Label(root, text=resstring).pack()
    root.geometry(resstring)


#designate original window wize
root.geometry("400x400")

#designate vertical slider
vertical = Scale(root, from_=200, to=800) #from requires the from_ underscore
vertical.pack() #make sure to pack it on its own line. scale widget are specific

#designate horizontal slider
horizontal = Scale(root, from_=200, to=800, orient=HORIZONTAL, command=update)
horizontal.pack()




btn = Button(root, text="update resolution", command=update).pack()



root.mainloop()