from tkinter import *
import sys
import os

root = Tk()
root.title("Breadnet")


img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)

#This thing below does not work for me at all
#root.iconbitmap('@/home/eein/fsl.png')


root.mainloop()