#!/usr/bin/env bash

if [[ -z "$CUSTOM_NODE_ID" ]]; then
    echo 'Using default node.id'
else
    echo "Using node.id: ${CUSTOM_NODE_ID}"
    sed -r -i "s@^#?node.id=.*@node.id=${CUSTOM_NODE_ID}@g" "/opt/kafka/config/kraft/server.properties"
fi

if [[ -z "$CUSTOM_LOG_DIRS" ]]; then
    echo 'Using default log.dirs'
else
    echo "Using log.dirs: ${CUSTOM_LOG_DIRS}"
    sed -r -i "s@^#?log.dirs=.*@log.dirs=${CUSTOM_LOG_DIRS}@g" "/opt/kafka/config/kraft/server.properties"
fi

if [[ -z "$CUSTOM_LISTENERS" ]]; then
    echo 'Using default listeners'
else
    echo "Using listeners: ${CUSTOM_LISTENERS}"
    sed -r -i "s@^#?listeners=.*@listeners=${CUSTOM_LISTENERS}@g" "/opt/kafka/config/kraft/server.properties"
fi

sed -i '/^advertised.listeners/d' /opt/kafka/config/kraft/server.properties

if [[ -z "$CUSTOM_INTER_BROKER_LISTENER_NAME" ]]; then
    echo 'Using default inter.broker.listener.name'
else
    echo "Using inter.broker.listener.name: ${CUSTOM_INTER_BROKER_LISTENER_NAME}"
    sed -r -i "s@^#?inter.broker.listener.name=.*@inter.broker.listener.name=${CUSTOM_INTER_BROKER_LISTENER_NAME}@g" "/opt/kafka/config/kraft/server.properties"
fi

sed -r -i "s@^#?listener.security.protocol.map=.*@listener.security.protocol.map=BROKER:PLAINTEXT,CONTROLLER:PLAINTEXT@g" "/opt/kafka/config/kraft/server.properties"

if [[ -z "$CUSTOM_ROLES" ]]; then
    echo 'Using default process.roles'
else
    echo "Using process.roles: ${CUSTOM_ROLES}"
    sed -r -i "s@^#?process.roles=.*@process.roles=${CUSTOM_ROLES}@g" "/opt/kafka/config/kraft/server.properties"
fi

if [[ -z "$CUSTOM_CONTROLLER_QUORUM_VOTERS" ]]; then
    echo 'Using default controller.quorum.voters'
else
    echo "Using controller.quorum.voters: ${CUSTOM_CONTROLLER_QUORUM_VOTERS}"
    sed -i "s/controller.quorum.voters=.*/controller.quorum.voters=${CUSTOM_CONTROLLER_QUORUM_VOTERS}/g" "/opt/kafka/config/kraft/server.properties"
fi

/opt/kafka/bin/kafka-storage.sh format \
    --cluster-id ${CLUSTER_ID:?} \
    -c /opt/kafka/config/kraft/server.properties \
    --ignore-formatted

/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/kraft/server.properties
