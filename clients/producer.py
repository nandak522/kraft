import os
import time
from confluent_kafka import Producer as ConfluentProducer
import logging
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer
from confluent_kafka.serialization import (
    StringSerializer,
    SerializationContext,
    MessageField,
)
from uuid import uuid4

from protobuf.events import order_placed_pb2

logging.basicConfig(level=logging.DEBUG)

BROKERS = os.getenv("BROKERS")
assert BROKERS

TOPIC = os.getenv("TOPIC")
assert TOPIC

SCHEMA_REGISTRY_HOST = os.getenv("SCHEMA_REGISTRY_HOST")
assert SCHEMA_REGISTRY_HOST


def main():
    producer_config = {
        "bootstrap.servers": BROKERS,
        "debug": "metadata,broker",
        "socket.keepalive.enable": True,
    }
    logging.debug("Producer Config:{}".format(str(producer_config)))

    kafka_producer = ConfluentProducer(producer_config)

    def delivery_callback(err, mesg):
        if err:
            logging.critical(
                "msg with id {} delivery err for partition:{} reason:{}".format(
                    str(mesg.key()), mesg.partition(), err
                )
            )
        else:
            logging.debug(
                "msg with id {} delivered to partition:{} offset:{}".format(
                    str(mesg.key()), mesg.partition(), mesg.offset()
                )
            )

    schema_registry_config = {"url": SCHEMA_REGISTRY_HOST}
    schema_registry_client = SchemaRegistryClient(schema_registry_config)
    protobuf_serializer = ProtobufSerializer(
        msg_type=order_placed_pb2.OrderPlaced,
        schema_registry_client=schema_registry_client,
        conf={"use.deprecated.format": False},
    )
    msg_key_serializer = StringSerializer("utf8")

    for i in range(10000):
        msg = order_placed_pb2.OrderPlaced(order_id=i, channel=0)
        logging.debug("Producing msg: {}".format(i))
        kafka_producer.produce(
            topic=TOPIC,
            key=msg_key_serializer(str(uuid4())),
            value=protobuf_serializer(
                msg, SerializationContext(TOPIC, MessageField.VALUE)
            ),
            on_delivery=lambda err, mesg: delivery_callback(err, mesg),
        )
        kafka_producer.flush()
        kafka_producer.poll(0)
        # time.sleep(0.5)


if __name__ == "__main__":
    main()
