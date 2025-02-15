import time
import threading
from typing import List

class Consumer:
    def __init__(self, shared_resources, interval: float, num_threads: int):
        self.shared_resources = shared_resources
        self.interval = interval
        self.num_threads = num_threads
        self.threads: List[threading.Thread] = []

    def consume(self, thread_id: int):
        while self.shared_resources.running:
            with self.shared_resources.lock:
                if not self.shared_resources.queue.empty():
                    number = self.shared_resources.queue.get()
                    print(f"[Consumer-{thread_id}] Processed: {number}")
            time.sleep(self.interval)

    def start(self):
        for i in range(self.num_threads):
            thread = threading.Thread(target=self.consume, args=(i,))
            self.threads.append(thread)
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()