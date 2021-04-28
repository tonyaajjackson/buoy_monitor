#!/bin/bash

set -a
source ../.env
set +a

echo "Waiting for Grafana to come online"
if ! ./wait-for grafana:3000; then
    exit
fi

echo "Grafana is online"

for i in data_sources/*; do
    curl -sS -X "POST" "http://grafana:3000/api/datasources" \
        -H "Content-Type: application/json" \
        --user $GRAFANA_USERNAME:$GRAFANA_PASSWORD \
        --data-binary @$i
done
printf '\nFinished POSTing data sources\n'
