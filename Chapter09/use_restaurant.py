from restaurant import Restaurant

my_restaurant = Restaurant("shunhou", "chinese")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(100)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(20)
print(my_restaurant.number_served)

