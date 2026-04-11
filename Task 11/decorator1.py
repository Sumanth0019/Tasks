def my_decorator(func):
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()