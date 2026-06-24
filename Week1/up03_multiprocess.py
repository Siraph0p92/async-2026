from time import sleep, ctime, time
import multiprocessing

def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")
    update_cup_number(customer_name)

def main():
    print(f"{ctime()} | === Multi-processing Coffee Machine ===")

    customers = ["A", "B", "C"]
    processes = []

    start = time()

    for customer in customers:
        p = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total = time() - start
    print(f"{ctime()} | Total time: {total:.2f} seconds")

if __name__ == "__main__":
    main()