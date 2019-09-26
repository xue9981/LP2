import json

def get_favorite_number():
    filename = "favorite.json"
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    filename = "favorite.json"
    # ask client's favorite number
    number = input("Please input your favorite number: ")
    
    # save client's favoirte number
    with open(filename, "w") as f_obj:
        json.dump(number, f_obj)

def get_user_number():
    number = get_favorite_number()
    if number:
        output_number(number)
    else:
        get_new_number()

def output_number(number):
    # output client's favorite number
    print("I know your favorite number! It's " + str(number))

get_user_number()
