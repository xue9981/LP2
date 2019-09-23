message = "Hello, this is Blue Sky Reastaurant."
message += "\nHow many in your party? "

num = int(input(message))

if num > 8:
    print("Sorry, there're no seats available.")
else:
    print("There're seats available.")
    
