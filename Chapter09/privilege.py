from user import User

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges: ")
        for privilege in self.privileges:
            print("\t-" + privilege)
