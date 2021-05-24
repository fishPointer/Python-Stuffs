from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer App')

img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)


my_img0 = ImageTk.PhotoImage(Image.open('/home/eein/Pictures/Anime Girls/1621501391821.jpg'))
my_img1 = ImageTk.PhotoImage(Image.open('/home/eein/Pictures/Anime Girls/1552029719191.png'))
my_img2 = ImageTk.PhotoImage(Image.open('/home/eein/Pictures/Anime Girls/unnamed.jpg'))

image_list = [my_img0, my_img1, my_img2]

my_label = Label(image=image_list[0])
my_label.grid(row=1, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<<", command=lambda: back(image_number-1))

    my_label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=0, column=0)
    button_next.grid(row=0, column=2)

    pass

def back():
    global my_label
    global button_forward
    global button_back
    pass

button_back = Button(root, text="<<<", command=back)
button_next = Button(root, text=">>>", command=lambda: forward(2))
button_exit = Button(root, text="Exit Program", command=root.quit)
#/home/eein/Pictures/Anime Girls/1550031776164.png


button_back.grid(row=0, column=0)
button_exit.grid(row=0, column=1)
button_next.grid(row=0, column=2)


root.mainloop()