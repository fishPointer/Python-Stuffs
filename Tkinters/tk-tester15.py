from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title('Breadbox GUI')
img = PhotoImage(file='/home/eein/Documents/Lab/Code/Python Stuffs/Tkinters/fsl.png')
root.call('wm', 'iconphoto', root._w, img)
root.geometry("400x400")



'''# This only needs to be run once, to create the file. it shouldn't be reran every time you run the script
#Create table
c.execute("""CREATE TABLE addresses ( 
        first_name text, 
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer 
        )
""")
'''

def submitFunction():
    #Databases
    #Create db or connection
    conn = sqlite3.connect('breadbook.db')

    #Create cursor instance
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :state, :city, :zipcode)",
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'state':state.get(),
                'city':city.get(),
                'zipcode':zipcode.get()

            })

    #Commit changes to db
    conn.commit()

    #Close Connection
    conn.close()

    # Clear Entry Fields
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    state.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    pass

def queryFunction():
    #Databases
    #Create db or connection
    conn = sqlite3.connect('breadbook.db')

    #Create cursor instance
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    #returns a python list containing a tuple of strings for each column of the database
    #[('Ian', 'Tralmer', 'Grayslake', 'Reno', 'NV', 89521, 1)]

    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    #Commit changes to db
    conn.commit()

    #Close Connection
    conn.close()
    pass

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

f_name_label = Label(root, text="First Name: ")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="Last Name: ")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address: ")
address_label.grid(row=2, column=0)
state_label = Label(root, text="State: ")
state_label.grid(row=3, column=0)
city_label = Label(root, text="City: ")
city_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode: ")
zipcode_label.grid(row=5, column=0)

submit_button = Button(root, text="Submit Data", command=submitFunction)
submit_button.grid(row=6, column=0, columnspan=2, ipadx=100)

query_button = Button(root, text="Query Database", command=queryFunction)
query_button.grid(row=7, column=0, columnspan=2, ipadx=100)






root.mainloop()