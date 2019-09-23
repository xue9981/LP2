prompt = "\nTo buy the ticket, Please input your age."
prompt += "\n(Enter 'quit' to finish) "

age = ''
active = True
fee = 0
while active:
    age = input(prompt)
    if age == 'quit':
        break
    elif int(age) < 3:
        fee = 0
    elif int(age) <= 12:
        fee = 10
    else:
        fee = 15

    print("Your ticket fee is $" + str(fee) + ".")

    
