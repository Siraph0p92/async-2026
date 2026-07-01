# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.

import asyncio
from time import time,ctime

async def cook_spagetthi(customer):
    print(f"{ctime()} -> Cooking for {customer}...")
    await asyncio.sleep(1)  # Simulating a time-consuming task (e.g., cooking).
    print(f"{ctime()} -> Served {customer}!")

async def main():
    start = time()


    task_a = asyncio.create_task(cook_spagetthi("A")) 
    task_b = asyncio.create_task(cook_spagetthi("B")) 
    
    print(f'{ctime()} -> Main program can do other things while Task A and Task B run in background.')

    await task_a # Awaiting the task to ensure it completes before moving on.
    await task_b # Awaiting the task to ensure it completes before moving on.

    print(f"Total Operation time: {time() - start:.2f} seconds") #will be around 2 seconds since we are awaiting each customer sequentially.

if __name__ == "__main__":
    asyncio.run(main())