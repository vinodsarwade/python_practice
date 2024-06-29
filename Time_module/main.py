'''time.time()'''
import time
# def using_while_loop():
#     i = 0
#     while i < 10000:
#         i = i + 1
#         print(i)

# def using_for_loop():
#     for i in range(10000):
#         print(i)

# init = time.time()
# using_for_loop()
# time_required = time.time() - init

# using_while_loop()
# print(time.time() - init) # time required for "while loop"
# print(time_required) # will print time required to print up to 10K for "for loop"


'''time.sleep()'''
# print(5)
# time.sleep(5)
# print("this will print after 5 seconds")


'''time.strftime()  -->staring formated time'''

t = time.localtime()
formated_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formated_time)
