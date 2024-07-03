
'''to use abstract class we need to import module  i.e: abstractmethod from  ABC'''
'''here we have made a Animal class is a abstract class, and in that class
we have created 'die' method as a abstract class method using @decorator. '''

'''now the thing is when you inherites this abstrcat class from child class we are getting errors bcz we dont have abstrcat method in each class.'''

'''to cover that we need to compulsury add the abstract merhod in inherited child class . then only it will run'''

'''here in this case in class bird and fish we have created 'die' method .'''
from abc import ABC, abstractmethod

class Animal(ABC):
    def eat(self):
        print("eating ...")
    
    @abstractmethod
    def die(self):
        pass

class Bird(Animal):
    def fly(self):
        print("flying...")
    def die(self):
        print("fish die on earth.!")

class Fish(Animal):
    def swim(self):
        print("swimming...")
    def die(self):
        print("learn swimming.!")

b = Bird()
b.eat()


# '''AI'''
# from abc import ABC, abstractmethod

# # Define the abstract class Animal
# class Animal(ABC):
#     def eat(self):
#         print("eating ...")
    
#     @abstractmethod  # Use the abstractmethod decorator to mark this method as abstract
#     def die(self):
#         pass  # Abstract methods typically do not provide an implementation

# # Define the Bird class that inherits from Animal
# class Bird(Animal):
#     def fly(self):
#         print("flying...")
    
#     def die(self):
#         print("Bird dies by falling from the sky.")

# # Define the Fish class that inherits from Animal
# class Fish(Animal):
#     def swim(self):
#         print("swimming...")
    
#     def die(self):
#         print("Fish dies out of water.")

# # Create instances of Bird and Fish and demonstrate their functionality
# b = Bird()
# b.eat()  # Calls the eat method from the Animal class
# b.fly()  # Calls the fly method from the Bird class
# b.die()  # Calls the die method from the Bird class

# f = Fish()
# f.eat()  # Calls the eat method from the Animal class
# f.swim()  # Calls the swim method from the Fish class
# f.die()  # Calls the die method from the Fish class
