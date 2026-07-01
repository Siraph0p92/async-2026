# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio 
from time import ctime, time 

async def cook_spaghetti(customer):
    print(f"{ctime()} -> cooking spaghetti for {customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()} -> spaghetti ready for {customer}!")

async def main():
    start_time = time()


    task_A = asyncio.create_task(cook_spaghetti("A"))    

    print(f"{ctime()}-> Main program can do other things while Task A runs in background.")

    await task_A

    print(f"Total Operation Time: {time() - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
