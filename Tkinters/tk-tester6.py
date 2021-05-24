from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer App')

img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)

global i
i = 0

def nextImage():
    global i
    i += 1
    if i > 2:
        i=0
    my_label = Label(image=image_list[i])
    my_label.grid(column=0, row=1)

    pass

my_img0 = ImageTk.PhotoImage(Image.open('/home/eein/Pictures/Anime Girls/1621501391821.jpg'))
my_img1 = ImageTk.PhotoImage(Image.open('/home/eein/Pictures/Anime Girls/1616640345773.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('/home/eein/Pictures/Anime Girls/unnamed.jpg'))

image_list = [my_img0, my_img1, my_img2]

#my_label = Label(image=my_img0)
#my_label.grid(column=0, row=1)

nextbutton = Button(text="Next Image", command=nextImage)
nextbutton.grid(column=0, row=0)
#/home/eein/Pictures/Anime Girls/1550031776164.png



root.mainloop()