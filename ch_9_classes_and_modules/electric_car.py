from car import Car
from battery import Battery

class ElectricCar(Car):

    def __init__(self, make, model):

        super().__init__(make, model)

        self.battery = Battery()