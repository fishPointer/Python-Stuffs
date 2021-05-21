# Calculator made with Tkinter for Python GUI tutorial
# May 21, 2021
# Ian Tralmer
from tkinter import *

#Set up window element
root = Tk()
root.title("Calculator")

#Define input field. You can actually type into this, but it's mainly for displaying calculator output
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#General 0-9 click response. Get clicked number, clear screen, append to running string of numbers, print
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

#Clear the screen
def button_clear():
    e.delete(0, END)
    return

#First number stored in global, pull second number. check global int for operation state, return
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if operation == 1:
        result = f_num+int(second_number)
    if operation == 2:
        result = f_num-int(second_number)
    if operation == 3:
        result = f_num*int(second_number)
    if operation == 4:
        result = f_num/int(second_number)
    e.insert(0, result)
    return

#Pull number and store to global cast as int, define operation state, clear screen
#Same function four times
def button_add():
    first_number = e.get()
    global f_num
    global operation
    operation = 1
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_subtract():
    first_number = e.get()
    global f_num
    global operation
    operation = 2
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_multiply():
    first_number = e.get()
    global f_num
    global operation
    operation = 3
    f_num = int(first_number)
    e.delete(0, END)
    return

def button_divide():
    first_number = e.get()
    global f_num
    global operation
    operation = 4
    f_num = int(first_number)
    e.delete(0, END)
    return


#Define button placement
#the padx margins vary I think because the characters have different widths
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=42, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=42, pady=20, command=button_divide)

button_eq = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=81, pady=20, command=button_clear)


#Render the buttons on the window in these grid positions
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_eq.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


#Keep the window open for interaction
root.mainloop()