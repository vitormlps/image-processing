
if __name__ == "__main__":
    from src.setup import setup_consumer


    consumer = setup_consumer()
    consumer.subscribe()
    consumer.start()
