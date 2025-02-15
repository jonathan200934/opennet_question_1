import time
from shared_resources import SharedResources
from producer import Producer
from consumer import Consumer
from config import Config

def run():
    shared_resources = SharedResources(Config.QUEUE_MAX_SIZE)

    producer = Producer(
        shared_resources,
        Config.PRODUCER_INTERVAL,
        Config.MIN_NUMBER,
        Config.MAX_NUMBER,
        Config.NUM_PRODUCERS
    )
    consumer = Consumer(
        shared_resources,
        Config.CONSUMER_INTERVAL,
        Config.NUM_CONSUMERS
    )

    try:
        print(f"Starting with {Config.NUM_PRODUCERS} producers and {Config.NUM_CONSUMERS} consumers...")
        producer.start()
        consumer.start()

        time.sleep(Config.PROGRAM_DURATION)
        shared_resources.stop()

        producer.join()
        consumer.join()
        print("Program completed successfully")

    except KeyboardInterrupt:
        print("\nReceived interrupt, shutting down...")
        shared_resources.stop()
        producer.join()
        consumer.join()

if __name__ == "__main__":
    run()