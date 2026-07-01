import asyncio
from time import sleep, ctime, time

# ---- Greeting: Synchronous (ทักทายทีละคน ไม่ขนาน) ----
def greet_dinners(customer):
    print(f"{ctime()}-> Greeting for Customer-{customer}...")
    sleep(1)
    print(f"{ctime()}-> Greeting for Customer-{customer}...Done!")

# ---- Task ต่อไปนี้เป็น async (ขนานข้ามลูกค้าได้) ----
async def take_orders(customer):
    print(f"{ctime()}->    [Task-{customer}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()}->    [Task-{customer}] Taking Order ...Done!")

async def do_cooking(customer):
    print(f"{ctime()}->    [Task-{customer}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{ctime()}->    [Task-{customer}] Cooking Spaghetti ...Done!")

async def mimi_bar(customer):
    print(f"{ctime()}->    [Task-{customer}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{ctime()}->    [Task-{customer}] Manage Bar for Drink ...Done!")

# ---- รวมขั้นตอนของลูกค้า 1 คน (เรียงลำดับภายในคนเดียวกัน) ----
async def serve_customer(customer):
    await take_orders(customer)
    await do_cooking(customer)
    await mimi_bar(customer)
    print(f"{ctime()}->    [Task-{customer}] All served!\n")

# ---- Main coroutine ----
async def main():
    customers = ['A', 'B', 'C']

    # 1) ทักทายทุกคนแบบ sync ก่อน (เรียงลำดับ)
    for customer in customers:
        greet_dinners(customer)

    print(f"{ctime()}-> --- All customers greeted. Scheduling independent Async Tasks! ---\n")

    # 2) เริ่มงานของทุกลูกค้าพร้อมกันแบบ async
    await asyncio.gather(*(serve_customer(c) for c in customers))

if __name__ == "__main__":
    start_time = time()
    asyncio.run(main())
    duration = time() - start_time
    print(f"{ctime()}-> Finished Entire Restaurant Operation in {duration:.2f} seconds.")