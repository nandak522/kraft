FROM ubuntu:22.04
ENV TZ=${TIMEZONE:-Asia/Kolkata}
ENV SCALA_VERSION 2.13
ENV KAFKA_VERSION 3.5.0

COPY download-kafka.sh /tmp/
WORKDIR /opt/kafka
COPY custom-start.sh /opt/kafka/bin/
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
