from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        self.sides = randint(1, 6)

    def roll_die_10(self):
        self.sides = randint(1, 10)

    def roll_die_20(self):
        self.sides = randint(1, 20)

my_die = Die()
result = []
for i in range(10):
    my_die.roll_die()
    result.append(my_die.sides)

result_10 = []
for i in range(10):
    my_die.roll_die_10()
    result_10.append(my_die.sides)

result_20 = []
for i in range(10):
    my_die.roll_die_20()
    result_20.append(my_die.sides)

print(result)
print(result_10)
print(result_20)

    
