from tkinter import *
#Python Image Library, Pillow
from PIL import ImageTk,Image

root = Tk()
root.title("Breadnet")


img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)

#This thing below does not work for me at all
#root.iconbitmap('@/home/eein/fsl.png')


my_img = ImageTk.PhotoImage(Image.open('/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png'))

my_label = Label(image=my_img)
my_label.pack()



button_quit = Button(root, text="Quit the Program", command=root.quit)
button_quit.pack()


root.mainloop()