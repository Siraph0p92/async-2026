from time import sleep, ctime, time

# ฟังก์ชันจำลองการชงกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)  # จำลองเวลาในการชงกาแฟ
    print(f"{ctime()} | Coffee ready for {customer_name}!")

# ฟังก์ชันจำลองการแสดงผลที่หน้าจอ LCD ของตู้กาแฟ
def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)  # จำลองเวลาในการประมวลผล/แสดงผลที่ LCD
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def main():
    queue = ['A', 'B', 'C']

    print(f"{ctime()} | === Synchronous Coffee Machine ===")
    start_time = time()

    # ทำงานตามลำดับคิวเดี่ยว (ทีละคน): ชงกาแฟ -> อัปเดต LCD
    for customer in queue:
        make_coffee(customer)
        update_cup_number(customer)

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds")

if __name__ == "__main__":
    main()