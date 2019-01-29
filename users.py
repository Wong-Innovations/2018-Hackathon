import json

class User:
    def __init__(self, username, password, email, active):
        self.username = username
        self.password = password
        self.email = email
        self.active = active

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email

    def set_active(self, active):
        self.active = active

    def store(self):
        with open('data/users.json') as file:
            users = json.load(file)
        users[self.username] = {'password': self.password, 'email': self.email, 'active': self.active}
        with open('data/users.json', 'w') as file:
            json.dump(users, file, indent=2)
