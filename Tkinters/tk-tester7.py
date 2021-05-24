from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Radio Button Tutorial')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)

frame = LabelFrame(root, text="This is my Frame.", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(root, text="button#1", command=root.quit)
b2 = Button(frame, text="button#Frame", command=root.quit)

b.pack()
b2.pack()

root.mainloop()
