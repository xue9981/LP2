class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Hello!\n" + "This is " + self.restaurant_name +
              " restaurant\n" + "Our cuisine type is " +
              self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant " + self.restaurant_name +
              " is open now!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
