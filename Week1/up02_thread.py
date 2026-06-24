from time import sleep, ctime, time
import threading

cup_number = 0
lock = threading.Lock()

def update_cup_number(customer_name):
    global cup_number
    with lock:
        cup_number += 1
        print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
        sleep(1)
        print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")
    update_cup_number(customer_name)

def main():
    print(f"{ctime()} | === Multi-threading Coffee Machine ===")
    
    customers = ["A", "B", "C"]
    threads = []
    
    start = time()
    
    for customer in customers:
        t = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    total = time() - start
    print(f"{ctime()} | Total time: {total:.2f} seconds")

if __name__ == "__main__":
    main()