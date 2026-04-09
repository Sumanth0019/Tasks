#method overriding
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
c = Cat()
d = Dog()


a.speak()
c.speak()
d.speak()