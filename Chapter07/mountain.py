responses = {}

# set a simbol to check continue or not
polling_active = True

while polling_active:
    # ask target's name and answer
    name = input("\nWhat is your name? ")
    response = input("Which mountain would your like to climb someday? ")

    # to save answers to a directory
    responses[name] = response

    # to check is there anyone still want to join this polling
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# finish polling and display the result
print("\n-- Poll Result --")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
    
