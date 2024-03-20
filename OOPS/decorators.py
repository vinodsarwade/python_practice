#decorator is a fucntion which  takes another function as a argument and and 
#changes it's behavior and return it

#it allows a programmer to modify or chnage behaviour of a function or class

def greet(fx):
    def mfx(*args , **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")

@greet
def add(a,b):
    print(a+b)

hello()
add(2,3)

