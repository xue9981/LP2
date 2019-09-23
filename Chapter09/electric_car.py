from car import Car
from battery import Battery

class ElectricCar(Car):
    """Electric car's features"""

    def __init__(self, make , model, year):
        """initialize parents' attribute"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Elctric cars don't have gas tank"""
        print("This car doesn't need a gas tank!")

    def upgrade_battery(self):
        if self.battery.battery_size != 85:
            self.battery.battery_size = 85

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
test_tesla = ElectricCar('test_tesla', 'model test', 2016)
test_tesla.battery.get_range()
test_tesla.upgrade_battery()
test_tesla.battery.get_range()


