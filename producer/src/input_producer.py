
from typing import Any, Dict
from time import sleep
from datetime import datetime, timezone, timedelta
import pickle

from confluent_kafka import Producer

from .camera import MP4File


class InputProducer:
    def __init__(self, config: Dict[str, Any], base_topic: str) -> None:
        self.producer = Producer(config)
        self.base_topic = base_topic


    @staticmethod
    def _delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: value (len) = {value}".format(
                topic=msg.topic(), 
                value=len(msg.value())
            ))


    def start(self, streaming_input: MP4File):
        print('Starting to produce the streaming input')

        tmz = timezone(-timedelta(hours=3))
        ts_format = '%Y-%m-%d_%H-%M-%S'
        input_type = streaming_input.name
        count = 0

        while True:
            topic = self.base_topic + "-" + str(count) # ex. input-processing-0

            success, data = streaming_input.read()

            if not success:
                continue

            value = pickle.dumps({
                'received_at': datetime.now(tmz).strftime(ts_format),
                'input_type': input_type,
                'input': data
            },
                protocol=pickle.HIGHEST_PROTOCOL
            )

            try:
                self.producer.produce(
                    topic=topic,
                    value=value, # bytes
                    on_delivery=InputProducer._delivery_callback
                )
            except Exception as err:
                print('ERROR: {}'.format(err))

            self.producer.poll(0)

            count += 1
            if count > 3:
                count = 0

            # sleep(0.5)
