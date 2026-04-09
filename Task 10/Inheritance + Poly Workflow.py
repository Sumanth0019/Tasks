#the contains workflow which combines both inheritance and polymorphism
# base Class
class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def calculate_toll(self):
        print("Base toll calculation")

    def display(self):
        print("Vehicle Number:", self.vehicle_number)


# child Class 1
class Car(Vehicle):
    def calculate_toll(self):
        toll = 50
        print("Car Toll:", toll)


# child Class 2
class Truck(Vehicle):
    def calculate_toll(self):
        toll = 150
        print("Truck Toll:", toll)


# child Class 3
class Bike(Vehicle):
    def calculate_toll(self):
        toll = 20
        print("Bike Toll:", toll)


def process_toll(vehicle):
    vehicle.display()
    vehicle.calculate_toll()
    print("----------------------")

# objects creation
v1 = Car("AP01AB1234")
v2 = Truck("AP02CD5678")
v3 = Bike("AP03EF9012")

# polymorphism
vehicles = [v1, v2, v3]

for v in vehicles:
    process_toll(v)