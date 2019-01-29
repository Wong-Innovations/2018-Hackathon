from tkinter import *
import tkinter.messagebox
import math
import json
import random
import atexit
from users import User
from shift import Shift


#----------------Initializing Variables-------------------
unit = 'half'
user = 0
with open('data/shifts.json') as file:
    shifts = json.load(file)
with open('data/users.json') as file:
    users = json.load(file)
#--------------------Sets Active User---------------------
for x in users:
    if (users[x]['active'] == True):
        user = x
positions = {}
positions[user] = {}
#---------------------------------------------------------

def commit_data(file_name, dictionary):
    with open(file_name, 'w') as file:
        json.dump(dictionary, file, indent=2)

#-------------------Position Handling---------------------
def print_pos():
    global user
    for names in positions[user]:
        write_to_box('''{}:
    ${} per 30 minutes.
    {} {}s are required to operate.\n'''.format(names, positions[user][names]['max_rev'], positions[user][names]['min_num'], names))

def add_position(name, max_rev, min_num):
    global user
    positions[user][name] = {'max_rev': 0, 'min_num': 0}
    positions[user][name]['max_rev'] = int(max_rev)
    positions[user][name]['min_num'] = int(min_num)
    erase_text_box()
    print_pos()

def edit_position(name, max_rev, min_num):
    global user
    positions[user][name]['max_rev'] = int(max_rev)
    positions[user][name]['min_num'] = int(min_num)
    erase_text_box()
    print_pos()

def delete_position(name):
    global user
    del positions[user][name]
    erase_text_box()
    print_pos()

def save_preset(name): # This function saves the current positions into a named preset to use later (JSON)
    with open('data/presets.json') as file:
        presets = json.load(file)
    presets[user] = {}
    presets[user][name] = {}
    presets[user][name] = positions[user]
    with open('data/presets.json', 'w') as file:
        json.dump(presets, file, indent=2)

def enter_addPos(input1, input2, input3): #function to input the info from "Add Position" tab
    if ((len(input1.get()) == 0) or (len(input2.get()) == 0) or (len(input3.get()) == 0)):
        error("One or more values are empty!")
    else:
        add_position(input1.get(), input3.get(), input2.get())
        root1.destroy()

def enter_editPos(input1, input2, input3): #function to input the info from "Add Position" tab
    if ((len(input1.get()) == 0) or (len(input2.get()) == 0) or (len(input3.get()) == 0)):
        error("One or more values are empty!")
    elif (input1.get() not in positions[user]):
        error("Could not find {} position".format(input1.get()))
    else:
        edit_position(input1.get(), input3.get(), input2.get())
        root1.destroy()

def enter_deletePos(input1):
    if (input1.get() not in positions[user]):
        error("Could not find {} position".format(input1.get()))
    else:
        delete_position(input1.get())
        root1.destroy()

def enter_savePre(input1):
    if (len(input1.get()) == 0):
        error("Invalid preset name.")
    else:
        save_preset(input1.get())
        root1.destroy()

def addPos():
    global root1, input1, input2, input3
    root1=Tk()
    root1.title("Add Position")
    root1.geometry("450x200+600+200")

    intruction = Label(root1, text="Enter Info:\n") # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=1) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    Label1 = Label(root1, text="Position Name: ") # This just does the same as above, instead with the text new username.
    Label2 = Label(root1, text="Minimum Positions Required: ")
    Label3 = Label(root1, text="Max Revenue Handled ($): ") # ^^

    Label1.grid(row=1, column=0, sticky = E) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    Label2.grid(row=2, column=0, sticky = E)
    Label3.grid(row=3, column=0, sticky = E)

    input1 = Entry(root1) # This now puts a text box waiting for input.
    input2 = Entry(root1)
    input3 = Entry(root1)
    input1.grid(row=1, column=1) # You know what this does now :D
    input2.grid(row=2, column=1) # ^^
    input3.grid(row=3, column=1)

    EnterButton = Button(root1, text="Enter", command=lambda: enter_addPos(input1, input2, input3))
    EnterButton.grid(row = 4, column = 2, columnspan=2, padx=3, pady=3)
    root1.mainloop() # This just makes the window keep open, we will destroy it soon

def editPos():
    global root1, input1, input2, input3
    root1=Tk()
    root1.title("Edit A Position")
    root1.geometry("450x200+600+200")

    intruction = Label(root1, text="Enter Info:\n") # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=1) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    Label1 = Label(root1, text="Position Name: ") # This just does the same as above, instead with the text new username.
    Label2 = Label(root1, text="Minimum Positions Required: ")
    Label3 = Label(root1, text="Max Revenue Handled ($): ") # ^^

    Label1.grid(row=1, column=0, sticky = E) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    Label2.grid(row=2, column=0, sticky = E)
    Label3.grid(row=3, column=0, sticky = E)

    input1 = Entry(root1) # This now puts a text box waiting for input.
    input2 = Entry(root1)
    input3 = Entry(root1)
    input1.grid(row=1, column=1) # You know what this does now :D
    input2.grid(row=2, column=1) # ^^
    input3.grid(row=3, column=1)

    EnterButton = Button(root1, text="Enter", command=lambda: enter_editPos(input1, input2, input3))
    EnterButton.grid(row = 4, column = 2, columnspan=2, padx=3, pady=3)
    root1.mainloop() # This just makes the window keep open, we will destroy it soon

def deletePos():
    global root1, input1
    root1=Tk()
    root1.title("Delete A Position")
    root1.geometry("270x120+600+200")

    intruction = Label(root1, text="Enter Info:\n") # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=1) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    Label1 = Label(root1, text="Position Name: ") # This just does the same as above, instead with the text new username.
    Label1.grid(row=1, column=0, sticky = E) # Same thing as the instruction var just on different rows. :) Tkinter is like that.

    input1 = Entry(root1) # This now puts a text box waiting for input.
    input1.grid(row=1, column=1) # You know what this does now :D

    EnterButton = Button(root1, text="Enter", command=lambda: enter_deletePos(input1))
    EnterButton.grid(row = 4, column = 2, columnspan=2, padx=3, pady=3)
    root1.mainloop() # This just makes the window keep open, we will destroy it soon

def presets_btn():
    global root1, input1
    root1=Tk()
    root1.title("Save A Preset")
    root1.geometry("270x120+600+200")

    intruction = Label(root1, text="Enter Info:\n") # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=1) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    Label1 = Label(root1, text="Preset Name: ") # This just does the same as above, instead with the text new username.
    Label1.grid(row=1, column=0, sticky = E) # Same thing as the instruction var just on different rows. :) Tkinter is like that.

    input1 = Entry(root1) # This now puts a text box waiting for input.
    input1.grid(row=1, column=1) # You know what this does now :D

    EnterButton = Button(root1, text="Enter", command=lambda: enter_savePre(input1))
    EnterButton.grid(row = 4, column = 2, columnspan=2, padx=3, pady=3)
    root1.mainloop() # This just makes the window keep open, we will destroy it soon
#---------------------------------------------------------

#--------------------Shift Handling-----------------------
def plan_shift(shift_name, start_time_hr, start_time_min, end_time_hr, end_time_min, rev_goal):
    global unit, user
    if (user not in shifts):
        shifts[user] = {}
    obj = Shift(user, shift_name, positions[user], shifts[user][shift_name], unit)
    for x in obj.numbers:
        write_to_box("{}: {}".format(x, obj.numbers[x]))

def enter_Planshift(name_var, first_hr, first_min, second_hr, second_min, variable1, variable2, rev_goal): #function to input the info from "Plan Shift" tab
    if (len(name_var.get()) == 0) or (len(first_hr.get()) == 0) or (len(first_min.get()) == 0) or (len(second_hr.get()) == 0) or (len(second_min.get()) == 0):
        error("One or more values are empty!")
    else:
        if (variable1 == 'PM'):
            start_time_hr = first_hr + 12
        else:
            start_time_hr = first_hr
        if (variable2 == 'PM'):
            end_time_hr = first_hr + 12
        else:
            end_time_hr = first_hr
        plan_shift(name_var, start_time_hr, first_min, end_time_hr, second_min, rev_goal)
        root1.destroy()

def planShift():
    global root1, name_var, first_hr, first_min, second_hr, second_min, variable1, variable2, rev_goal#to get the AM/PM selection, use variable1.get()
    root1=Tk()
    root1.title("Plan a shift")
    root1.geometry("450x200+600+200")

    intruction = Label(root1, text="Enter Shift Info:\n") # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=3) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    #AM/PM dropdown box

    variable1 = StringVar(root1)
    variable1.set("AM") # default value
    variable2 = StringVar(root1)
    variable2.set("AM") # default value

    AMPM1 = OptionMenu(root1, variable1, "AM", "PM")
    AMPM2 = OptionMenu(root1, variable2, "AM", "PM")
    Name = Label(root1, text="Name: ") # This just does the same as above, instead with the text new username.
    Start = Label(root1, text="Start: ")
    End = Label(root1, text="End: ") # ^^
    colon1 = Label(root1, text=":")
    colon2 = Label(root1, text=":")
    Rev = Label(root1, text="Goal: ")

    Name.grid(row=1, column=0, sticky = E) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    Start.grid(row=2, column=0, sticky = E)
    End.grid(row=3, column=0, sticky = E)

    #********Enrty boxes************

    name_var = Entry(root1) #Name
    first_hr = Entry(root1) #first hour
    first_min = Entry(root1) #first min
    second_hr = Entry(root1) #second hour
    second_min = Entry(root1) #second min
    rev_goal = Entry(root1)

    #*******Placements**********

    name_var.grid(row=1, column=1)
    first_hr.grid(row=2, column=1)
    colon1.grid(row=2, column=2)
    first_min.grid(row=2, column=3)
    second_hr.grid(row=3, column=1)
    colon2.grid(row=3, column=2)
    second_min.grid(row=3, column=3)
    AMPM1.grid(row=3, column=4)
    AMPM2.grid(row=2, column=4)
    Rev.grid(row=4, column=0, sticky = E)
    rev_goal.grid(row=4, column=1)

    EnterButton = Button(root1, text="Enter", command=lambda: enter_Planshift(name_var, first_hr, first_min, second_hr, second_min, variable1, variable2, rev_goal))
    EnterButton.grid(row = 5, column = 8, columnspan=2, padx=3, pady=3)
    root1.mainloop() # This just makes the window keep open, we will destroy it

#---------------------------------------------------------

def doNothing():
    print("Nothing!")
    error("You just did nothing!")

def error(message):
    tkinter.messagebox.showerror('Error', message)

def PosOptions():
    Plan_Shift_Button.grid_forget()
    View_Shift_Button.grid_forget()
    Add_Pos_Button.grid(row = 1, column = 0, sticky = W, padx=10, pady=5)
    Edit_Pos_Button.grid(row = 2, column = 0, sticky = W, padx=10, pady=5)
    Delete_Pos_Button.grid(row = 3, column = 0, sticky = W, padx=10, pady=5)
    Presets_Pos_Button.grid(row = 0, column = 0, sticky = W, padx =10, pady = 10)

def ShiftsOptions():
    Add_Pos_Button.grid_forget()
    Edit_Pos_Button.grid_forget()
    Delete_Pos_Button.grid_forget()
    Presets_Pos_Button.grid_forget()
    Plan_Shift_Button.grid(row = 1, column = 0, sticky = W, padx=10, pady=5)
    View_Shift_Button.grid(row = 2, column = 0, sticky = W, padx=10, pady=5)


def viewShifts():
    print("Nothing")

def write_to_box(string):
    text.config(state="normal")
    text.insert(INSERT,string)
    text.config(state="disabled")

def erase_text_box():
    text.config(state="normal")
    text.delete('1.0', END)
    text.config(state="disabled")

def exit():
    root.destroy()

def exit_handler():
    users[user]['active'] = False
    commit_data('data/users.json', users)
atexit.register(exit_handler)

######################################################################################################################################



######################################################################################################################################


root = Tk()
root.title("Shift Program")
root.geometry("600x600+500+100")


#***************MENU BAR*************************

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)

menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)

#*****************Frames************************

toolbar = Frame(root, bg="#666b65", width = 600, height = 50)
first_selection = Frame(root, width=50, height=50, padx=3, pady=3)
second_selection = Frame(root, width=50, height=50, padx=3, pady=3)
window = Frame(root, width=50, height=50, padx=40, pady=40)

#layout of root container
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


# create all of the main containers
toolbar.grid(row = 0, sticky="ew")
first_selection.grid(row=1, sticky="nw")
second_selection.grid(row=2, sticky="w")
window.grid(row=1, sticky="se")

#create preset widget
second_selection.grid_rowconfigure(2, weight=1)
second_selection.grid_columnconfigure(0, weight=1)
#***************Toolbar Buttons*************************

positionbutton = Button(toolbar, text="Positions", command=PosOptions)
positionbutton.grid(row = 0, column = 0, padx=2, pady=2)
shiftbutton = Button(toolbar, text="Shifts", command=ShiftsOptions)
shiftbutton.grid(row = 0, column = 1, padx=2, pady=2)
shiftbutton = Button(toolbar, text="Exit", command=exit)
shiftbutton.grid(row = 0,column = 2, padx=2, pady=2)

#****************Selection Buttons*********************

Add_Pos_Button = Button(first_selection, text="ADD POSITION", command=addPos)
Edit_Pos_Button = Button(first_selection, text="EDIT POSITION", command=editPos)
Delete_Pos_Button = Button(first_selection, text="DELETE POSITION", fg="red", command=deletePos)
Presets_Pos_Button = Button(second_selection, text="PRESETS", fg = "#9900ff", command=presets_btn)

Plan_Shift_Button = Button(first_selection, text="PLAN A SHIFT", command=planShift)
View_Shift_Button = Button(first_selection, text="VIEW MY SHIFTS", command=viewShifts)

PosOptions()

#**************Text Window****************************


#window.grid_rowconfigure(1, weight=1)
#window.grid_columnconfigure(3, weight=1)
text = Text(window, width = 40, height = 50)
text.config(state="disabled")
text.grid()


root.mainloop()
