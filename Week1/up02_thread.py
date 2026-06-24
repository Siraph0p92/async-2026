from time import sleep, ctime, time
import threading

# ฟังก์ชันจำลองการชงกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)  # จำลองเวลาในการชงกาแฟ
    print(f"{ctime()} | Coffee ready for {customer_name}!")

# ฟังก์ชันจำลองการแสดงผลที่หน้าจอ LCD ของตู้กาแฟ
def update_lcd(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)  # จำลองเวลาในการประมวลผล/แสดงผลที่ LCD
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

# ฟังก์ชันรวมงานของลูกค้า 1 คน (ชงกาแฟ -> อัปเดต LCD) ให้รันใน Thread เดียวกัน
def serve_customer(customer_name):
    make_coffee(customer_name)
    update_lcd(customer_name)

def main():
    queue = ['A', 'B', 'C']

    print(f"{ctime()} | === Multi-threading Coffee Machine ===")
    start_time = time()

    threads = []
    # สร้าง Thread แยกให้ลูกค้าแต่ละคน ทำงานพร้อมกัน
    for customer in queue:
        t = threading.Thread(target=serve_customer, args=(customer,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds")

if __name__ == "__main__":
    main()