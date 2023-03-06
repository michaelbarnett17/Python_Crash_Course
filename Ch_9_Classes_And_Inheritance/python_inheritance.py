from pydoc import describe


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0

    def get_descriptive_name(self):
        long_name = f"{ self.make } { self.model } { self.year }"
        return long_name

    def read_odomoter(self):
        print(f"This car has { self.odomoter_reading } miles on it.")

    def update_odomoter(self, milage):
        self.odomoter_reading = milage

class ElectricCar(Car):

    def __init__(self, make, model, year):

        super().__init__(make, model, year)

        self.battery = Battery()





class Battery:

    def __init__(self, size = 40):

        self.size = size
        
    def describe_battery(self):
        print(f"The battery size of this car is { self.size }")

    def get_range(self):

        if self.size == 40:
            range = 150

        elif self.size == 60:
            range = 225

        return range




my_leaf = ElectricCar("nissian", "ultima", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
print(f"The range is { my_leaf.battery.get_range() }.")