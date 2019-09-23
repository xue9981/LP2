def greet_User(username):
    """display plain greeting"""
    print("Hello!, " + username.title() + "!")

greet_User('jesse')

def get_formatted_name(first_name, last_name):
    """return full name"""
    full_name = first_name + ' ' + last_name
    return full_name

active = True
# this is a loop
while active:
    print("\nPlease tell me your name")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name.title() + "!")
    active = input("Is there any other people? (yes/no) ")
    while True:
        if active == 'no':
            active = False
            break
        elif active == 'yes':
            break
        else:
            active = input("Is there any other people? (yes/no) ")
