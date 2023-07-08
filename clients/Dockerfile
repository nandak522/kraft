FROM ubuntu:22.04

RUN apt-get clean && \
    apt-get update && \
    apt-get install -y --no-install-recommends build-essential \
    lsof \
    netcat \
    net-tools \
    python3-dev \
    python3-pip \
    python-setuptools \
    software-properties-common \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN wget --no-check-certificate https://github.com/edenhill/librdkafka/archive/v2.1.1.zip && unzip -q v2.1.1.zip && rm v2.1.1.zip && cd librdkafka-2.1.1 && ./configure && make && make install && ldconfig \
    && pip install -r /app/requirements.txt
ENV BROKERS=localhost:9092
ENV TOPIC=test
CMD ["python"]
