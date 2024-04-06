#decorator is a fucntion which  takes another function as a argument and
#changes it's behavior and return it

#it allows a programmer to modify or chnage behaviour of a function or class

def greet(fx):
    def mfx(*args , **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thanks for using this function\n")
    return mfx

@greet
def hello():
    print("hello world")

@greet
def add(a,b):
    print(a+b)

hello()
add(2,3)


#example 2

'''In Python, decorators are a powerful feature that allows you to add functionality to an existing function or class. 
Decorators are implemented using the @ symbol followed by the decorator function's name, placed above the function or class definition.'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
'''In this example:
We define a decorator function called my_decorator. This function takes another function func as its argument.
Inside my_decorator, we define a nested function wrapper that adds some functionality before and after calling the original function func.
We then use the @my_decorator syntax to decorate the say_hello function. This means that when say_hello is called, it will actually call my_decorator(say_hello) instead.
When say_hello is called, it invokes my_decorator, which in turn calls the wrapper function, executing the additional functionality before and after calling say_hello itself.'''
