# Delivery System): นักศึกษาต้องเขียน try...except CancelledError ได้ถูกต้อง 
# และใช้ .get_name(), .cancel(), และ .cancelled() ได้
# smart_courier.py
# Assignment 1: Smart Courier System (40 คะแนน)
import asyncio
from time import ctime

async def delivery_task(package_id: str, duration: float):
    """
    จำลองการส่งพัสดุ ใช้เวลา `duration` วินาที
    ถ้าถูกยกเลิกระหว่างทาง (CancelledError) ให้พิมพ์ข้อความแล้ว re-raise
    เพื่อให้ task จบสถานะเป็น cancelled จริง ๆ
    """
    print(f"[{ctime()}] Courier started delivering {package_id}...")
    try:
        await asyncio.sleep(duration)
        print(f"[{ctime()}] Package {package_id} Delivered!")
        return f"Package {package_id} Delivered!"
    except asyncio.CancelledError:
        print(f"[{ctime()}] Delivery Canceled! Returning package to warehouse.")
        raise  # re-raise เพื่อให้ Task จบสถานะเป็น cancelled อย่างสมบูรณ์


async def main():
    # 2. สร้าง Task และตั้งชื่อว่า "Express-Courier"
    task = asyncio.create_task(
        delivery_task("P001", 5.0),
        name="Express-Courier"
    )

    # 3. รอ 2 วินาที แล้วเช็คว่า task เสร็จหรือยัง
    await asyncio.sleep(2)
    print(f"[{ctime()}] Checking task '{task.get_name()}'. Is it done? {task.done()}")

    # 4. ถ้ายังไม่เสร็จ (ใช้เวลานานเกินไป) ให้ยกเลิกทันที
    if not task.done():
        print(f"[{ctime()}] Taking too long! Canceling the task...")
        task.cancel()

    # รอให้ task จบการทำงานจริง ๆ (ไม่ว่าจะ cancel หรือเสร็จ)
    try:
        await task
    except asyncio.CancelledError:
        pass

    # 5. ตรวจสอบสถานะภายนอกว่า cancelled() เป็น True หรือไม่
    print(f"[{ctime()}] Final verify: Is task officially canceled? {task.cancelled()}")


if __name__ == "__main__":
    asyncio.run(main())