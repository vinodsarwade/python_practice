'''multiple task can be executed at a same time without any blocking.
multiple threads can run in a single process.so it wont take much time.'''

'''The goal of multithreading is to complete multiple tasks at the same time, which improves application rendering and performance.'''

import threading
import time

def fun(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

# #normal code,(it takes more time to run this function one by one)
# fun(4)
# fun(3)
# fun(1)

#using threading  
t1 = threading.Thread(target=fun,args=[4])
t2 = threading.Thread(target=fun,args=[3])
t3 = threading.Thread(target=fun,args=[1])

#to start the thrade
t1.start()
t2.start()
t3.start()

# #waiting for threads to complete
# t1.join()
# t2.join()
# t3.join()


#ex: 2 AI
import threading
import time

# Function to print numbers from 1 to 5
def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1: {i}")
        time.sleep(1)

# Function to print letters from A to E
def print_letters():
    for char in ['A', 'B', 'C', 'D', 'E']:
        print(f"Thread 2: {char}")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Both threads have finished execution.")


'''The following are the advantages of using Python for multithreading:

It guarantees powerful usage of PC framework assets.
Applications with multiple threads respond faster.
It is more cost-effective because it shares resources and its state with sub-threads (child).
It makes the multiprocessor engineering more viable because of closeness.
By running multiple threads simultaneously, it cuts down on time.
To store multiple threads, the system does not require a lot of memory.'''

