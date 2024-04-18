'''Certainly! The concurrent.futures module in Python provides a high-level interface for asynchronously executing callables. One of the useful classes it offers is ThreadPoolExecutor, which allows you to manage a pool of threads and submit tasks to be executed concurrently. This is beneficial for scenarios where you need to execute multiple tasks concurrently but want to limit the number of threads created'''

import concurrent.futures
import time

# Function to simulate a task that takes some time to complete
def task(name):
    print(f"Task {name} is starting...")
    time.sleep(2)  # Simulate some time-consuming operation
    print(f"Task {name} is done.")

# Create a ThreadPoolExecutor with a maximum of 2 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(1, 6)]

    # Wait for all tasks to complete
    for future in concurrent.futures.as_completed(futures):
        try:
            future.result()  # Get the result of the completed task (or raise exception if any)
        except Exception as e:
            print(f"An error occurred: {e}")
