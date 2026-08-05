import asyncio
import time
import httpx

# ==========================================
# 1. Configuration & Constants
# ==========================================
STUDENT_ID = "6710301036" 
BASE_URL = "http://172.16.2.117:8088"

# กำหนดลำดับชิ้นส่วนและหุ่นยนต์
PARTS = ["A", "B", "C"]
ROBOTS = ["robot_1", "robot_2", "robot_3", "robot_4"]

# ==========================================
# 2. Async Functions Development
# ==========================================

async def reset_factory(client: httpx.AsyncClient):
    """ส่ง Request เพื่อทำการ Reset สถานะของหุ่นยนต์ทั้งหมดของรหัสนักเรียนนี้"""
    await asyncio.sleep(0.5)
    await client.post(f"/student/{6710301036}/reset")

async def grab_part(client: httpx.AsyncClient, robot_id: str, part: str):
    """สั่งให้หุ่นยนต์หยิบชิ้นส่วน 1 ชิ้น"""
    await asyncio.sleep(0.5)
    await client.post(f"/student/{6710301036}/robot/{robot_id}/grab",
        json={"part A ": part},
    )

async def run_robot_task(client: httpx.AsyncClient, robot_id: str):
    """สั่งให้หุ่นยนต์ 1 ตัว ทำการหยิบชิ้นส่วน A, B, และ C ตามลำดับ"""
    for part in PARTS:
        print(f"{robot_id} is grabbing part {part}...")
        await grab_part(client, robot_id, part )  

async def main():
    """ฟังก์ชันหลักสำหรับเริ่มการทำงานของหุ่นยนต์ทั้ง 4 ตัวแบบ Async"""
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=10.0) as client:
        print("Resetting Factory...")
        await reset_factory(client)
        
        start_time = time.time()
        print("หุ่นยนต์กำลังทำงานทั้งหมด")
        
        await asyncio.gather(*(run_robot_task(client, robot_id) for robot_id in ROBOTS))
        
        elapsed_time = time.time() - start_time
        print(f"Finished all tasks in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())