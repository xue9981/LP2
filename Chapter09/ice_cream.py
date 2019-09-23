from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, stand_name, cuisine_type, flavor):
        super().__init__(stand_name, cuisine_type)
        self.flavor = flavor

    def flavor_name(self):
        print("Our flavor is " + self.flavor + ".")

    def open_restaurant(self):
        print("IceCreamStand " + self.restaurant_name +
              " is open now!")

my_icecream = IceCreamStand('relax', 'western', 'soda')
my_icecream.open_restaurant()
my_icecream.set_number_served(100)
print(my_icecream.number_served)
my_icecream.increment_number_served(100)
print(my_icecream.number_served)
my_icecream.flavor_name()
    
