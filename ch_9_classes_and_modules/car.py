class Car:

    def __init__ (self, make, model):

        self.make = make
        self.model = model

    def get_descriptive_name(self):
        long_name = f"{ self.make } { self.model } { self.year }"
        return long_name

    def read_odomoter(self):
        print(f"This car has { self.odomoter_reading } miles on it.")

    def update_odomoter(self, milage):
        self.odomoter_reading = milage