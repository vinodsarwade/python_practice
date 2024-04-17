'''asyncio is a library to write concurrent code using the async/await syntax.'''

# import asyncio
# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')

# asyncio.run(main())

#Ex: 2
import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("fun 1")

async def function2():
    await asyncio.sleep(1)
    print("fun 2")

async def function3():
    await asyncio.sleep(1)
    print("fun 3")

async def main():
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
   
asyncio.run(main())

#Ex :3 AI
import asyncio

async def say_hello(delay, name):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    # Schedule coroutines to run concurrently
    task1 = asyncio.create_task(say_hello(2, "Alice"))
    task2 = asyncio.create_task(say_hello(1, "Bob"))

    # Wait for all tasks to complete
    await asyncio.gather(task1, task2)

asyncio.run(main())

