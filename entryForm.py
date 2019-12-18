# import tkinter module
from tkinter import *
from tkinter.ttk import *
import bot
import json

# creating main tkinter window/toplevel
master = Tk()
#we will store entries in this array
entries = []

# this wil create a label widget
l0 = Label(master, text = "Serial")
l1 = Label(master, text = "Name:")
l2 = Label(master, text = "Gender:")
l3 = Label(master, text = "Nationality:")
l4 = Label(master, text = "ID Type:")
l5 = Label(master, text = "ID No:")
l6 = Label(master, text = "Number of Camera:")

# entry widgets, used to take entry from user


# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 1, sticky = W, pady = 2)
l2.grid(row = 0, column = 2, sticky = W, pady = 2)
l3.grid(row = 0, column = 3, sticky = W, pady = 2)
l4.grid(row = 0, column = 4, sticky = W, pady = 2)
l5.grid(row = 0, column = 5, sticky = W, pady = 2)
l6.grid(row = 0, column = 6, sticky = W, pady = 2)

# this will arrange entry widgets
for i in range(20):
    entry = []
    e0 = Label(master, text = int(i+1))
    e1 = Entry(master)
    e1.insert(i, ' ')

    e2 = StringVar(master)
    e2.set('--select--')
    e2_entry = OptionMenu(master, e2, '--select--', "Male", "Female", "Transgender")

    e3 = StringVar(master)
    e3.set('--select--')
    e3_entry = OptionMenu(master, e3, '--select--', "Indian", "Foreigner")

    e4 = StringVar(master)
    e4.set("--select--")
    e4_entry = OptionMenu(master, e4, '--select--', "Passport", "Aadhar", "Driving Licence", "Voter ID", "PAN Card", "Office ID", "Student ID")

    e5 = Entry(master)
    e5.insert(i, ' ')
    e6 = Entry(master)
    e6.insert(i, 0)
    entry.append(e1)
    entry.append(e2)
    entry.append(e3)
    entry.append(e4)
    entry.append(e5)
    entry.append(e6)
    e0.grid(row = i+1, column=0, sticky = 'nsew', pady=2 )
    e1.grid(row = i+1, column = 1, pady = 2)
    e2_entry.grid(row = i+1, column = 2, pady = 2)
    e3_entry.grid(row = i+1, column = 3, pady = 2)
    e4_entry.grid(row = i+1, column = 4, pady = 2)
    e5.grid(row = i+1, column = 5, pady = 2)
    e6.grid(row = i+1, column = 6, pady = 2)
    entries.append(entry)
# infinite loop which can be terminated by keyboard

table_values = LabelFrame(master, text="Values", borderwidth=10, relief=GROOVE)
data_readout = Button(master, text="Submit", command=lambda: readData())
data_readout.grid(column=6, row=21)


def readData():
#    for i in entries:
#        for j in i:
#            print(j.get())
    bot.runbot(entries)

mainloop()