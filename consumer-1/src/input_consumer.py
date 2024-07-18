
from typing import Any, Dict

from confluent_kafka import Consumer

from src.image import save_image


class InputConsumer:
    def __init__(self, config: Dict[str, Any], topic_to_subs: str) -> None:
        self.consumer = Consumer(config)
        self.topic_to_subs = topic_to_subs


    def subscribe(self):
        print("Subscribing to topic")

        self.consumer.subscribe([self.topic_to_subs])


    def start(self):
        print("Starting to consume produced input from topic")

        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            save_image(msg)

        self.consumer.close()
