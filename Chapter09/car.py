"""car model"""

class Car():
    """chanllenge to simulate car"""

    def __init__(self, make, model, year):
        """initialeze car's attribute"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.battery = Battery()

    def get_descriptive_name(self):
        """return car's description"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """print an infomation about car's odometer"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        set odometer's value
        and refuse to back the odometer
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """increment the odometer's value"""
        self.odometer_reading += miles

class Battery():
    """challenge to simulate battery"""

    def __init__(self, battery_size=70):
        """initialize print an infomation about battery"""
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) +
              "-kWh battery.")

    
    def get_range(self):
         """print about range"""
         if self.battery_size == 70:
             range = 240
         elif self.battery_size == 85:
             range = 270

         message = "This car can go approximately " + str(range)
         message += " miles on a full charge."
         print(message)

class ElectricCar(Car):
    """simulate Electric car"""

    def __init__(self, make, model, year):
        """
        initialize parents' attribute and 
        initialize Electric car's attribute
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        

        
        
