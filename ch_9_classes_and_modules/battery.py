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