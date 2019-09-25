import json

def greet_user():
    # if you saved data, load it.
    # Or informe your user to add his/her name.
    """greet user, and print his/her name"""
    filename = 'username.json'
    try: 
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " +
            username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()


