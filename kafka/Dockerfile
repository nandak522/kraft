FROM ubuntu:22.04
ENV TZ=${TIMEZONE:-Asia/Kolkata}
ENV SCALA_VERSION 2.13
ENV KAFKA_VERSION 3.5.0
ENV JMX_PROMETHEUS_JAVAAGENT_VERSION 0.19.0
ENV JMX_PROMETHEUS_JAVAAGENT_DOMAIN https://repo1.maven.org

COPY download-kafka.sh /tmp/
WORKDIR /opt/kafka
COPY custom-start.sh /opt/kafka/bin/
COPY jmx-prom-java-agent-config.yaml /opt/kafka/jmx-prom-java-agent-config.yaml
ADD ${JMX_PROMETHEUS_JAVAAGENT_DOMAIN}/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/${JMX_PROMETHEUS_JAVAAGENT_VERSION}/jmx_prometheus_javaagent-${JMX_PROMETHEUS_JAVAAGENT_VERSION}.jar /opt/kafka/jmx_prometheus_javaagent.jar
RUN apt-get update && apt-get install -y --no-install-recommends gpg-agent wget software-properties-common && \
    wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | apt-key add - && \
    add-apt-repository --yes https://packages.adoptium.net/artifactory/deb && \
    apt-get install -y --no-install-recommends temurin-20-jdk libnet-rawip-perl libnet-pcap-perl libnetpacket-perl less lsof netcat net-tools wget

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ >/etc/timezone && \
    chmod a+x /tmp/download-kafka.sh && \
    /tmp/download-kafka.sh && \
    tar xfvz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz --strip-components 1 -C /opt/kafka && \
    chmod +x /opt/kafka/bin/custom-start.sh && \
    rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz && \
    rm -rf /var/lib/apt/lists/*
VOLUME /opt/kafka-kraft-data
CMD [ "/opt/kafka/bin/custom-start.sh" ]
