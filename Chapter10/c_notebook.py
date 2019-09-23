filename = "learning_python.txt"

with open(filename) as file_object:
    content = file_object.read().replace('Python', 'C')
    print(content.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.replace("Python", "C").rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace("Python", "C").rstrip())
