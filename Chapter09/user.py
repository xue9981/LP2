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

shunhou = User("shunhou", "sen")
shunhou.greet_user()
nakatani = User("yuta", "nakatani")
nakatani.greet_user()
nagi = User("nagi", "nakamura")
nagi.greet_user()

for i in range(0, 1000):
    shunhou.increment_login_attempts()

print(shunhou.login_attempts)

shunhou.reset_login_attempts()

print(shunhou.login_attempts)
