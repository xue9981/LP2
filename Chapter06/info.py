sen = {"first_name": "JunFeng", "last_name": 'Xue', "age": 21, "city": "Saitama"}

nagi = {"first_name": "nagi", "last_name": 'Nakamura', "age": 21, "city": "Keio Univ."}

nakatani = {"first_name": "yuta", "last_name": "nakatani", "age": 21, "city": "Tokyo Univ."}

people = [sen, nagi, nakatani]

print(type(nakatani["age"]))

for person in people:
    for info in person.keys():
        print(info + ": " + str(person[info]).title())

    print("\n")

        



