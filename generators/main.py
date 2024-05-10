'''generators in python are special type of function that allow you to create an iterable sequence of values.
a generator function returns a generator object. which can be used to generate the values one by one as you iterate over it.
it allow you to generate the values on the fly,rather than having to create and store the entire sequence in memory.'''

'''it doesnt store value ,it stores the required data to generate a genarative object.'''

#in python you can create a generator by using the 'yield' statement in function.
#the yield statement returns the value from the generator and suspends the execution of function.untill the next value is requested.

'''Ex : 1'''
def my_generator():
    for i in range(500):
        yield i

gen = my_generator()
print(next(gen)) #print 0
print(next(gen)) #print 1
print(next(gen)) #print 2
# ir will generate o/p only once, we need to increase generative objects.

'''Ex : 2'''
def my_generator():
    for i in range(500):
        yield i

gen = my_generator()
for j in gen:
    print(j)


'''Ex : 3'''
# Generator expression
gen = (x * 2 for x in range(3))

# Using the generator
print(next(gen))  # Output: 0
print(next(gen))  # Output: 2
print(next(gen))  # Output: 4


