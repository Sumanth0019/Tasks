class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")


birds = [Sparrow(), Ostrich()]

for b in birds:
    b.fly()