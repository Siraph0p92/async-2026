from time import ctime, time
import asyncio

# ฟังก์ชันจำลองการชงกาแฟให้ลูกค้า 1 คน (แบบ Asynchronous)
async def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1)  # จำลองเวลาในการชงกาแฟ (Non-blocking)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

# ฟังก์ชันจำลองการแสดงผลที่หน้าจอ LCD ของตู้กาแฟ (แบบ Asynchronous)
async def update_lcd(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1)  # จำลองเวลาในการประมวลผล/แสดงผลที่ LCD (Non-blocking)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

# ฟังก์ชันรวมงานของลูกค้า 1 คน (ชงกาแฟ -> อัปเดต LCD) ให้รันใน Coroutine เดียวกัน
async def serve_customer(customer_name):
    await make_coffee(customer_name)
    await update_lcd(customer_name)

async def main():
    queue = ['A', 'B', 'C']

    print(f"{ctime()} | === Asyncio Coffee Machine ===")
    start_time = time()

    # สร้าง Task ให้ลูกค้าแต่ละคน ทำงานพร้อมกันบน Event Loop เดียว
    tasks = [asyncio.create_task(serve_customer(customer)) for customer in queue]

    # สั่งให้ทุก Task ทำงานพร้อมกัน
    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())