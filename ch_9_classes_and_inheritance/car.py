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


my_new_car = Car("audi", "a4", 2023)

print(my_new_car.get_descriptive_name())

my_new_car.read_odomoter()
my_new_car.odomoter_reading = 55
my_new_car.read_odomoter()

my_new_car.update_odomoter(100)
my_new_car.read_odomoter()


