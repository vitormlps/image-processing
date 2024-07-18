
from .input_consumer import InputConsumer


def setup_consumer():
    print('Setting up consumer')

    msg_size = 10 * 1048576
    config = {
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'bigdata-images',
        'auto.offset.reset': 'earliest',
        'message.max.bytes': msg_size,
        'max.partition.fetch.bytes': msg_size,
        'fetch.max.bytes': msg_size,
    }
    topic_to_subs = 'input-processing-0'

    return InputConsumer(config, topic_to_subs)
