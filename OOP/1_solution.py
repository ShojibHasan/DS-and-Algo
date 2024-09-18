class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCard(Car):
    def __init__(self,battery_size):
        self.battery_size = battery_size
    