import asyncio
from time import ctime, time, sleep

async def greet_diners(customer):
    print(f"{ctime()}  Greeting for Customer-{customer}...")
    await asyncio.sleep(1)
    print(f"{ctime()}  Greeting for Customer-{customer} ...Done!")

async def customer_private_workflow(customer):
    # Take Order
    print(f"{ctime()}  [Task-{customer}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()}  [Task-{customer}] Taking Order ...Done!")

    # Do Cooking
    print(f"{ctime()}  [Task-{customer}] Cooking Spaghetti...")
    await asyncio.sleep(1)
    print(f"{ctime()}  [Task-{customer}] Cooking Spaghetti...Done!")

    # Mini Bar
    print(f"{ctime()}  [Task-{customer}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{ctime()}  [Task-{customer}] Manage Bar for Drink ...Done!")
    print(f"{ctime()}  [Task-{customer}] all Served!\n")

async def main():
    start = time()
    customers = ["A", "B", "C"]


    await greet_diners("A")
    await greet_diners("B")
    await greet_diners("C")

    print(f"\n{ctime()}  --- All Customer greeted. Scheduling independent Async Tasks! ---\n")

    # Start private workflows for each customer
    await asyncio.gather(*(customer_private_workflow(customer) for customer in customers))
    duration = time() - start
    print(f"{ctime()}  Finish Entire restaurant Operation in {duration:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
