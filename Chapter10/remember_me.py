import json

def get_stored_username():
    """if you saved username, print it"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """inform user to input his/her name"""
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username

def ask_user(username):
    if username == None:
        return None
    while True:
        msg = "Are you " + username + "? (yes/no) "
        answer = input(msg)
        if answer == "yes":
            return username
        elif answer == "no":
            return None
               
def greet_user():
    # if you saved data, load it.
    # Or informe your user to add his/her name.
    """greet user, and print his/her name"""
    username = get_stored_username()
    username = ask_user(username)
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
    
greet_user()


