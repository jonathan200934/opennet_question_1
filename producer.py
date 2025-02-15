import random
import time
import threading
from typing import List

class Producer:
    def __init__(self, shared_resources, interval: float, min_num: int, max_num: int, num_threads: int):
        self.shared_resources = shared_resources
        self.interval = interval
        self.min_num = min_num
        self.max_num = max_num
        self.num_threads = num_threads
        self.threads: List[threading.Thread] = []

    def produce(self, thread_id: int):
        while self.shared_resources.running:
            with self.shared_resources.lock:
                if not self.shared_resources.queue.full():
                    number = random.randint(self.min_num, self.max_num)
                    self.shared_resources.queue.put(number)
                    print(f"[Producer-{thread_id}] Generated: {number}")
            time.sleep(self.interval)

    def start(self):
        for i in range(self.num_threads):
            thread = threading.Thread(target=self.produce, args=(i,))
            self.threads.append(thread)
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()