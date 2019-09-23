class Dog():
    """challenge to simulate dog"""

    def __init__(self, name, age):
        """initialize name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate sit pose"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """simulate roll over pose"""
        print(self.name.title() + " rolled over")


my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#print(my_dog)

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + "years old.")
your_dog.sit()

print(my_dog)
print(your_dog)

