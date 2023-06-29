## What you get
* A 3 node Kafka cluster
    * kafka1:19092
    * kafka2:29092
    * kafka3:39092
* [Up to date Kafka](https://github.com/nandak522/kraft/blob/main/Dockerfile#L4)
* [Up to date OpenJDK Java(20) from Adoptium](https://github.com/nandak522/kraft/blob/main/Dockerfile#L11)
* Running in KRaft mode (without ZooKeeper)
* A simple GUI to browse topics and msgs, powered by [Kafdrop](https://github.com/obsidiandynamics/kafdrop)
    * Head over to http://localhost:9000 in your favorite browser

### Build
```sh
docker build -t local/kafka-base:v3.5.0 .
```

## Run
```sh
docker compose up kafka1 kafka2 kafka3 kafdrop
```
`kafka1`, `kafka2` and `kafka3` use the above common/base image `local/kafka-base:v3.5.0`
