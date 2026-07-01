# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.

import asyncio
from time import time,ctime
from tracemalloc import start

async def serve_customer(name):
    print(f"{ctime()} -> Serving customer {name}")
    await asyncio.sleep(1)
    print(f"{ctime()} -> Done serving customer {name}!")

async def main():
    start_time = time()
    customers = ["A", "B", "C", "D"]
    task_list = []  # This will hold all the tasks we create.

    for name in customers:
        t = asyncio.create_task(serve_customer(name))  # Create a task for each customer.
        task_list.append(t)  # Append the task to the list.
    

    await asyncio.gather(*task_list)  # Awaiting all tasks to ensure they complete before moving on.

if __name__ == "__main__":
    asyncio.run(main())