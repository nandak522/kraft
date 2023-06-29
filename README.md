### What you get
* A 3 node Kafka cluster
    * kafka1:19092
    * kafka2:29092
    * kafka3:39092
* (Up to date Kafka)[https://github.com/nandak522/kraft/blob/main/Dockerfile#L4]
* (Up to date Java(17) from Adoptium)[https://github.com/nandak522/kraft/blob/main/Dockerfile#L11]
* Running in KRaft mode (without ZooKeeper)
* A simple GUI to browse topics and msgs, powered by (https://github.com/obsidiandynamics/kafdrop)[Kafdrop]
    * Head over to http://localhost:9000 in your favorite browser

### Run
```sh
docker compose up --build kafka1 kafka2 kafka3 kafdrop
```
kafka1, kafka2, kafka3 all use a common image called `local/kafka-base:v3.5.0`
