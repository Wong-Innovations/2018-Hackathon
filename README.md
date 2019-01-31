# 2018 Hackathon

20hr tkinter/python app submission to the 2018 Fox Optimization Hackathon. Coded by Cameron Cobb, Gage Christensen, and Dylan Wong.

## The Challenge

Hackathon contestants were posed with the task to make an app which an employer could use to schedule shifts, save shiftss and minimize resources without impacting revenue.

## Our Aproach

As a team we all had the most experience with tkinter for creating python backed GUIs, while the library is both limited and dated we made due. We then programed an object oriented model to handle every shift, user, and employee. Lastly we knew being able to perminatly save data was a must for this project, and while none of us had experience using SQL databases we sere still able to recreate the functionality using JSON documents (which python can easily parse). The following was our workflow:
- [x] Build shifts model
- [x] Build users model
- [x] Link shift objects to user accounts
- [x] Implement data saving/loading
- [x] Build the GUI
- [x] Connect the GUI to the backend using Lambda functions
- [ ] Add an email account-recovery system

### login\.py

```python
def CheckLogin(rootA, usernameE, confpwordE):
    with open('data/users.json') as file: # Pulls the JSON dictionary of current users
        users = json.load(file)
    if (usernameE.get() in users) and confpwordE.get() == users[usernameE.get()]['password']: # Checks to see if you entered the correct data.
        rootA.destroy() #Enter the login window below
        import GUI # We know what bad practice this is but we were desperate
    else:
        error("Invalid Login!")
```

We methodically implimented input validation and custom responses, as to increase the intuitiveness of the app.

```python
def CreateButton(rootB, usernameE, emailE, pwordE, confpwordE):
    if ((len(usernameE.get()) == 0) or (len(emailE.get()) == 0) or (len(pwordE.get()) == 0) or (len(confpwordE.get())==0)):
        error("One or more input fields are empty!")
    elif (pwordE.get() != confpwordE.get()):
        error("Passwords do not match!")
    else:
        obj = User(usernameE.get(), confpwordE.get(), emailE.get(), True)
        obj.store()
        user = obj.username
        rootB.destroy() # Destroys the signup window
        Login() # Respawns login home
```
