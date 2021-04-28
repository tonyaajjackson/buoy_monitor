while true; do
    date
    for buoy_id in {0..9}; do
        python ./monitor/monitor.py \
            --graphite-host 127.0.0.1 \
            --graphite-port 2004 \
            --buoy-id buoy_${buoy_id} \
            --lat 58.232067 \
            --lon -13${buoy_id}
        echo "Sending buoy_${buoy_id}"
        sleep 1
    done
    sleep 5
done