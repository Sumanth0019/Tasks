#without using any of the class & Obj
def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def display_result(name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    
    print("Student:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)

name = "Rahul"
marks = [85, 90, 78]

display_result(name, marks)