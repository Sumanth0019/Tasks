#OOPs one using class and objects

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display_result(self):
        print("Student:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())


# object
student1 = Student("Rahul", [85, 90, 78])

# Calling methods
student1.display_result()