# lights.py
import asyncio
import httpx
from time import perf_counter

BASE_URL = "http://172.16.2.117:8088"
STUDENT_ID = "6710301036"
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]

async def turn_on_light(client: httpx.AsyncClient, light_id: str):
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    response = await client.post(url, json={"status": "ON"})
    return light_id, response.status_code

async def main():
    start = perf_counter()

    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [
            asyncio.create_task(turn_on_light(client, light_id))
            for light_id in LIGHT_IDS
        ]

        # gather จะคืนผลลัพธ์เรียงตามลำดับที่ใส่ใน tasks เสมอ (ไม่ว่าจะเสร็จก่อนหลังยังไง)
        results = await asyncio.gather(*tasks)

        for light_id, status_code in results:
            print(f"{light_id} -> {status_code}")

    elapsed = perf_counter() - start
    print(f"\nเปิดไฟทั้งหมด เสร็จใน {elapsed:.2f} วินาที")

if __name__ == "__main__":
    asyncio.run(main())