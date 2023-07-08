import os
from confluent_kafka import Consumer as ConfluentConsumer
from confluent_kafka import KafkaError as ConfluentKafkaError
import logging
import socket

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

BROKERS = os.getenv("BROKERS")
assert BROKERS

TOPIC = os.getenv("TOPIC")
assert TOPIC

CONSUMER_GROUP = os.getenv("CONSUMER_GROUP")
assert CONSUMER_GROUP

CONSUMER_INSTANCE_ID = os.getenv("CONSUMER_INSTANCE_ID")
assert CONSUMER_INSTANCE_ID


def main():
    host = socket.gethostname()

    def on_commit_callback(error, partitions):
        if error:
            logger.debug(
                "[{}] on_commit_callback error:{} partitions:{}".format(
                    host, error, str(partitions)
                )
            )

    def print_assignments(consumer, partitions):
        logger.debug(
            "{} consumer latest assignments:{}".format(consumer, str(partitions))
        )

    consumer_config = {
        "bootstrap.servers": BROKERS,
        "debug": "metadata",
        # 'debug': 'metadata,cgrp',
        "group.id": CONSUMER_GROUP,
        # 'group.instance.id': CONSUMER_INSTANCE_ID,
        "heartbeat.interval.ms": 1000,
        "socket.keepalive.enable": True,
        "socket.timeout.ms": 5000,
        "session.timeout.ms": 6000,
        "enable.auto.commit": True,
        "auto.offset.reset": "earliest",
        "on_commit": on_commit_callback,
    }
    logger.debug("[{}] Consumer Config:{}".format(host, str(consumer_config)))
    consumer = ConfluentConsumer(consumer_config)

    consumer.subscribe([TOPIC], on_assign=print_assignments)
    logger.debug(
        "[{}] Subscribed to {} topic and waiting for msgs...".format(host, TOPIC)
    )
    try:
        while 1:
            msg_obj = consumer.poll(timeout=1.0)
            if not msg_obj:
                logger.debug("[{}] Waiting for next msg...".format(host))
                continue
            elif (
                msg_obj.error()
                and msg_obj.error().code() != ConfluentKafkaError._PARTITION_EOF
            ):
                logger.error("[{}] error:{}".format(host, str(msg_obj.error())))
                break
            else:
                logger.debug(
                    "[{}] Consumer Received msg_obj: {} at partition:{} offset:{}".format(
                        host,
                        str(msg_obj.value()),
                        msg_obj.partition(),
                        msg_obj.offset(),
                    )
                )
                if not consumer_config["enable.auto.commit"]:
                    try:
                        consumer.commit(async=True)
                    except Exception as e:
                        logger.error(
                            "[{}] Error in committing! Reason:{}".format(host, str(e))
                        )
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
