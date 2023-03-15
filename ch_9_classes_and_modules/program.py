from car import Car
from electric_car import ElectricCar


my_car = Car("ford", "mustang")

print(my_car.make)
print(my_car.model, end="\n\n")

my_electric_car = ElectricCar("ferarri", "911")

print(my_electric_car.make)
print(my_electric_car.model)
print(f"The range is { my_electric_car.battery.get_range() }")