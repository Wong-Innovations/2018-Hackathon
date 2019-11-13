# I (Cameron Cobb) also made this file.

from tkinter import *
import tkinter.messagebox
import json
from users import User

def error(message):
    tkinter.messagebox.showerror('Error', message)

def createaccount(rootA):
    rootA.destroy()
    global usernameE, emailE, pwordE, confpwordE

    rootB = Tk() # This creates the window, just a blank one.
    rootB.title('Create Account') # This renames the title of said window to 'signup'
    rootB.geometry('300x150+600+200')
    intruction = Label(rootB, text='Enter New Credidentials:\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=2) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    username = Label(rootB, text="New Username: ") # This just does the same as above, instead with the text new username.
    email = Label(rootB, text="Email: ")
    pword = Label(rootB, text="New Password: ") # ^^
    confpword = Label(rootB, text="Confirm Password: ")
    username.grid(row=1, column=1, sticky = E) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    email.grid(row=2, column=1, sticky = E) # ^^
    pword.grid(row=3, column=1, sticky = E)
    confpword.grid(row=4, column=1, sticky = E)

    usernameE = Entry(rootB) # This now puts a text box waiting for input.
    emailE = Entry(rootB)
    pwordE = Entry(rootB, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    confpwordE = Entry(rootB, show='*')
    usernameE.grid(row=1,column=2, sticky=E) # This now puts a text box waiting for input.
    emailE.grid(row=2,column=2, sticky=E)
    pwordE.grid(row=3,column=2, sticky=E)
    confpwordE.grid(row=4,column=2, sticky=E)
     # ^^

    CreateAccButton = Button(rootB, text='Create', command=lambda: CreateButton(rootB, usernameE, emailE, pwordE, confpwordE)) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    CreateAccButton.grid(row=5, column=3, padx=5,pady=5)

    #signupButton.grid(columnspan=2)
    rootB.mainloop() # This just makes the window keep open, we will destroy it soon

def Login(): # This is the signup definition,
    global usernameE, emailE, pwordE, confpwordE

    rootA = Tk() # This creates the window, just a blank one.
    rootA.title('Login') # This renames the title of said window to 'signup'
    rootA.geometry('300x150+600+200')
    intruction = Label(rootA, text='Enter Credidentials:\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=2) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    nameL = Label(rootA, text='Username: ') # This just does the same as above, instead with the text new username.
    pwordL = Label(rootA, text='Password: ') # ^^
    nameL.grid(row=1, column=1, sticky = E) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=1, sticky = E) # ^^

    usernameE = Entry(rootA) # This now puts a text box waiting for input.
    confpwordE = Entry(rootA, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    usernameE.grid(row=1, column=2) # You know what this does now :D
    confpwordE.grid(row=2, column=2) # ^^

    LoginButton = Button(rootA, text='Login', command=lambda: CheckLogin(rootA, usernameE, confpwordE)) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    LoginButton.grid(row=3, column=2, padx=5,pady=5)

    CreateAccButton = Button(rootA, text='Create Account', command=lambda: createaccount(rootA)) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    CreateAccButton.grid(row=3, column=1, padx=5,pady=5)

    #signupButton.grid(columnspan=2)
    rootA.mainloop() # This just makes the window keep open, we will destroy it soon

def CreateButton(rootB, usernameE, emailE, pwordE, confpwordE):
    if ((len(usernameE.get()) == 0) or (len(emailE.get()) == 0) or (len(pwordE.get()) == 0) or (len(confpwordE.get())==0)):
        error("One or more input fields are empty!")
    elif (pwordE.get() != confpwordE.get()):
        error("Passwords do not match!")
    else:
        obj = User(usernameE.get(), confpwordE.get(), emailE.get(), True)
        obj.store()
        user = obj.username
        rootB.destroy() # This will destroy the signup window. :)
        Login() # This will move us onto the login definition :D

def CheckLogin(rootA, usernameE, confpwordE):
    with open('data/users.json') as file: # Pulls the JSON dictionary of current users
        users = json.load(file)
    if (usernameE.get() in users) and confpwordE.get() == users[usernameE.get()]['password']: # Checks to see if you entered the correct data.
        rootA.destroy() #Enter the login window below
        import GUI # We know what bad practice this is but we were desperate
    else:
        error("Invalid Login!")

Login()
