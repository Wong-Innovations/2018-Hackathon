# 2018 Hackathon

20hr tkinter/python app submission to the 2018 Fox Optimization Hackathon. Coded by Cameron Cobb, Gage Christensen, and Dylan Wong.

## The Challenge

Hackathon contestants were posed with the task to make an app which an employer could use to schedule shifts, save shiftss and minimize resources without impacting revenue.

## Our Aproach

As a team we all had the most experience with tkinter for creating python backed GUIs, while the library is both limited and dated we made due. We then programed an object oriented model to handle every shift, user, and employee. Lastly we knew being able to perminatly save data was a must for this project, and while none of us had experience using SQL databases we sere still able to recreate the functionality using JSON documents. The following was our workflow:
- [x] Build shifts model
- [x] Build users model
- [x] Link shift objects to user accounts
- [x] Implement data saving/loading
- [x] Build the GUI
- [x] Connect the GUI to the backend using Lambda functions
- [ ] Add an email account-recovery system

### login\.py

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

### GUI.py

The following code demonstrates how complex tkinter GUI elements are, this is where our workflow could've been expediated the most through the use of a better library such as QT.

```python
input1 = Entry(root1) # This and more has to be repeated for each element of the GUI
input2 = Entry(root1)
input3 = Entry(root1)
input1.grid(row=1, column=1)
input2.grid(row=2, column=1)
input3.grid(row=3, column=1)
```

On a positive note, serializing the data for saving and manipulating was very easy due to the similarities between JSON and Python dictionaries.

```python
def save_preset(name): # This function saves the current positions into a named preset to use later
    with open('data/presets.json') as file:
        presets = json.load(file)
    presets[user] = {}
    presets[user][name] = {}
    presets[user][name] = positions[user]
    with open('data/presets.json', 'w') as file:
        json.dump(presets, file, indent=2)
```

### shifts.py

Now we've arived to the real "meat and potatos" of our application. The shift object model is very complex, but elegant, its what allows for customization down to 12hr/24hr clocks.

```python
class Shift:
    def __init__(self, username, shift_name, positions, shift, unit):
        self.username = username
        self.shift_name = shift_name
        self.positions = positions
        # ...
```
