import requests
import time

BASE = "http://172.16.2.117:8088"
STUDENT_ID = "6710301036"
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]


def turn_on(light_id):
    url = f"{BASE}/api/{STUDENT_ID}/lights/{light_id}"
    resp = requests.post(url, json={"status": "ON"})
    print(f" {light_id} -> {resp.status_code}")
    return resp.json()


def main():
    start = time.perf_counter()

    # เปิดไฟทีละดวงตามลำดับ 1 → 2 → 3 → 4
    for light_id in LIGHT_IDS:
        turn_on(light_id)

    elapsed = time.perf_counter() - start
    print(f"\n  เปิดไฟทั้งหมดเสร็จใน {elapsed:.2f} วินาที")


if __name__ == "__main__":
    main()