def read_animal(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
#        print("Sorry, but file '" + filename + "' does not exist!")
        pass
    else:
        print(contents.rstrip())

filenames = ['dog.txt', 'cat.txt', 'bird.txt']
for filename in filenames:
    read_animal(filename)
