# pets info
pet_1 = {"type": "dog", "master": "john"}
pet_2 = {"type": "cat", "master": "cathy"}
pet_3 = {"type": "lion", "master": "miya"}

# pets list
pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for key in pet.keys():
        print(str(key) + ": " + str(pet[str(key)].title()))

    # goto nextline when you finish to print out about one of the
    # pet in list pets
    print("\n")


