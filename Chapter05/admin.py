#users = ['turuoka', 'watanabe', 'nakatani', 'negisi', 'admin']
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ', would you like to see a status report?')
        else:
            print("Hello " + user.title() + ', thank you for logging in login')
else:
    print("We need to find users!")


        
