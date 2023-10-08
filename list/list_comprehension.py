#list comprehension means on the fly generate a new list

lst =[i*i for i in range(5)]    # it will create a list up to 5 while iterating each element is multiply by i
print(lst)

lst =[i*i for i in range(5) if i%2==0]  #newly created list  which has elements divisible by 2 and its modulus is 0
print(lst)                              #those elements is only added in list;