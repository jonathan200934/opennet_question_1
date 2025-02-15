# shared_resources.py
import queue
import threading

class SharedResources:
    def __init__(self, queue_size):
        self.queue = queue.Queue(maxsize=queue_size)
        self.lock = threading.Lock()
        self.running = True

    def stop(self):
        self.running = False