class Battery():
    """Challenge to simulate battery"""
    def __init__(self, battery_size=70):
        """initialize battery's attribute"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print infomation about battery"""
        print("This car has a " + str(self.battery_size) + \
              "-kWh battery")

    def get_range(self):
        """print about infomation about distance"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
