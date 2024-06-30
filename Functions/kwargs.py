#this is a normal code which takes keywords arguments as a parameter.
#and return a dictionary object , but here in below case it will return only value from fun.

# def add_student(**args):
#     for x in args:
#         print(x)  # to get value use like print(args[x]) 

# add_student(name="vinod", rollNo= 12, age = 24)




def add_student(**args):
    for x, y in args.items(): #here in this case we used two variable x and y to store the key and value in args. to get both value we use ".items()" from kwargs.
        print(f"{x} = {y}")

add_student(name="vinod", rollNo= 12, age = 24)
