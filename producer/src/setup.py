
from .input_producer import InputProducer
from .camera import MP4File


def setup_producer():
    print('Setting up producer')

    msg_size = 10 * 1048576
    config = {
        'bootstrap.servers': 'kafka:9092',
        'message.max.bytes': msg_size,
    }
    base_topic = 'input-processing'

    return InputProducer(config, base_topic)


def setup_streaming_input():
    print('Setting up streaming input')

    input = MP4File()
    input.setup()

    return input
