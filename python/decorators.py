import functools

def my_decorator(func):
    @functools.wraps(func)
    def my_decorator_wrap():
        print("Before my_decorator_wrap")
        func()
        print("after my_decorator_wrap")
    return my_decorator_wrap



@my_decorator
def my_function():
    print("Hi im calling function")


my_function()