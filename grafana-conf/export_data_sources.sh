set -a
source ../.env
set +a

mkdir -p data_sources
curl -s "http://localhost:3000/api/datasources" \
    -u $GRAFANA_USERNAME:$GRAFANA_PASSWORD \
    | jq -c -M '.[]' \
    | split -l 1 - data_sources/