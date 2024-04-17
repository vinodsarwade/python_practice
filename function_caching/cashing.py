'''Function caching in Python refers to the technique of storing the results of expensive function calls 
and returning the cached result when the same inputs occur again.
This can significantly improve the performance of applications by avoiding redundant computations.'''

#method 1 using lru_cache (useful when simple and efficient way to cache function result without managing cache manually)
from functools import lru_cache
import time

@lru_cache(maxsize= None)
def fx(n):
    time.sleep(5)
    return n * 5

'''first it will compute for below valuesas time of 5 sec.each '''
print(fx(5))
print("done for 5")
print(fx(10))
print("done for 10")
print(fx(3))
print("done for 3")


'''but here in below case we are going to provide same value ,which is already computed, so this cached result will print fastlt without stopping 5 sec.'''
print(fx(5))
print("done for 5")
print(fx(2))
print("done for 2")
print(fx(3))
print("done for 3")



#method 2 using dictionary  (manually managing cache as per requirment so it gives more control.)
def cached_function(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@cached_function
def expensive_function(x):
    # Some expensive computation
    return x * x

print(expensive_function(5))  # Computes and caches result
print(expensive_function(5))  # Returns cached result
