
if __name__ == '__main__':
    from src.setup import (
        setup_producer,
        setup_streaming_input
    )


    producer = setup_producer()
    streaming_input = setup_streaming_input()

    producer.start(streaming_input)
