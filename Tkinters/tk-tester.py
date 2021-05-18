from tkinter import *



root = Tk()

#This defines the label
myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="This is my pretty boy swag")
#can be done this way
# myLabel2 = Label(root, text="This is my pretty boy swag").grid(row=0, column=0)

myButton = Button(root, text="Click Me!")





#This Renders the Labels
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=1, column=1)

#The window close X button interrupts this loop
root.mainloop()
