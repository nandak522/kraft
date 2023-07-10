## What you get
* A 3 node Kafka cluster
    * kafka1:19092
    * kafka2:29092
    * kafka3:39092
* [Up to date Kafka](https://github.com/nandak522/kraft/blob/main/Dockerfile#L4)
* [Up to date OpenJDK Java(20) from Adoptium](https://github.com/nandak522/kraft/blob/main/Dockerfile#L11)
* Running in KRaft mode (without ZooKeeper)
* A simple GUI to browse topics and msgs, powered by [Kafka-UI from provectuslabs](https://github.com/provectuslabs/kafka-ui)
    * Head over to http://localhost:8080 in your favorite browser

### Build
```sh
docker build -t local/kafka-base:v3.5.0 .
```

## Run
```sh
docker compose up kafka1 kafka2 kafka3 kafka-ui
```
`kafka1`, `kafka2` and `kafka3` use the above common/base image `local/kafka-base:v3.5.0`

### Test using Metrics
```sh
PORT=39999
unset KAFKA_JMX_OPTS && unset JMX_PORT && /opt/kafka/bin/kafka-run-class.sh org.apache.kafka.tools.JmxTool \
  --one-time true \
  --jmx-url service:jmx:rmi:///jndi/rmi://:${PORT}/jmxrmi \
  --object-name kafka.controller:type=KafkaController,name=ActiveControllerCount
```
The above command should give an output like:
```sh
Trying to connect to JMX url: service:jmx:rmi:///jndi/rmi://:39999/jmxrmi
time,"1688110063561"
kafka.controller:type=KafkaController,name=ActiveControllerCount:Value,"1"
```

P.S: Above `unset`ting of certain env vars is because running the above `kafka-run-class.sh` command with `JMX_PORT` being set is throwing a weird `Port/Address already in use` exception.
