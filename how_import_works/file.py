import math
result = math.sqrt(9)
print(result)

#or we can write like this below
#if we using from math then  we dont need to use math. 
from math import sqrt, pi
result=sqrt(9) * pi
print(result) 

#we can import all the function from module using *
#ex: from math import *   ; this is not recommanded bcz interpreter will confuse and getting warning


#as keyword
from math import sqrt as s # we can replace sqrt by s only ...and we can use only s rather than sqrt in code
result = s(9) * pi
print(result)

#dir function
import math
print(dir(math))  # it will get all  the function from math module