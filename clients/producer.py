import os
import time
from confluent_kafka import Producer as ConfluentProducer
import logging

logging.basicConfig(level=logging.DEBUG)

BROKERS = os.getenv("BROKERS")
assert BROKERS

TOPIC = os.getenv("TOPIC")
assert TOPIC

def main():
    producer_config = {
        'bootstrap.servers': BROKERS,
        'debug': 'metadata,broker',
        'socket.keepalive.enable': True
    }
    logging.debug("Producer Config:{}".format(str(producer_config)))
    
    kafka_producer = ConfluentProducer(producer_config)

    def delivery_callback(err, mesg):
        if err:
            logging.critical("msg:{} delivery err for partition:{} reason:{}".format(mesg.value(), mesg.partition(), err))
        else:
            logging.debug("msg:{} delivered to partition:{} offset:{}".format(mesg.value(), mesg.partition(), mesg.offset()))

    for i in range(10000):
        msg = "Test Msg {}".format(i)
        logging.debug("Producing msg: {}".format(i))
        kafka_producer.produce(TOPIC, msg, callback=lambda err, mesg: delivery_callback(err, mesg))
        kafka_producer.flush()
        kafka_producer.poll(0)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
