class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges: ")
        for privilege in self.privileges:
            print("\t-" + privilege)

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        self.user_name = self.first_name.title() + " " +\
                                self.last_name.title()
        return self.user_name

    def greet_user(self):
        print("Hello, " + self.describe_user() + "!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)

shunhou = Admin("shunhou", "sen",
                ["can add post",
                 "can delete post",
                 "can ban user"])

shunhou.greet_user()
shunhou.privileges.show_privileges()
                
