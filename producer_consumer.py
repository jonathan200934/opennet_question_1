import threading
import queue
import time
import random

shared_queue = queue.Queue(maxsize=10)
lock = threading.Lock()
running = True

def producer():
    while running:
        with lock:
            if not shared_queue.full():
                number = random.randint(1, 100)
                shared_queue.put(number)
                print(f"Produced: {number}")
        time.sleep(0.1)

def consumer():
    while running:
        with lock:
            if not shared_queue.empty():
                number = shared_queue.get()
                print(f"Consumed: {number}")
        time.sleep(0.15)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

time.sleep(10)
running = False

producer_thread.join()
consumer_thread.join()

print("Program completed")