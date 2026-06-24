from time import sleep, ctime, time
import multiprocessing

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

# ฟังก์ชันรวมงานของลูกค้า 1 คน (ชงกาแฟ -> อัปเดต LCD) ให้รันใน Process เดียวกัน
def serve_customer(customer_name):
    make_coffee(customer_name)
    update_lcd(customer_name)

def main():
    queue = ['A', 'B', 'C']

    print(f"{ctime()} | === Multi-processing Coffee Machine ===")
    start_time = time()

    processes = []
    # สร้าง Process แยกให้ลูกค้าแต่ละคน ทำงานพร้อมกันแบบแยกหน่วยประมวลผลเด็ดขาด
    for customer in queue:
        p = multiprocessing.Process(target=serve_customer, args=(customer,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds")

if __name__ == "__main__":
    main()