import threading
import time

def worker(first, last):
    time.sleep(2)
    print(f"{first} {last} started the work")

def mail():
    time.sleep(4)
    print("You got the mail")

c1 = threading.Thread(target=worker, args=("shahid", "khan"))
c1.start()

c2 = threading.Thread(target=mail)
c2.start()

c1.join()
c2.join()

print("Your tasks are completed")