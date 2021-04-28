import argparse
from datetime import datetime
import pickle
import random
import socket
import struct

# CLI Arg parsing
parser = argparse.ArgumentParser(
    usage='%(prog)s [OPTION] [VALUE]'
)
parser.add_argument(
    '--graphite-host',
    help='Hostname of the Graphite server listening for monitoring messages',
    action='store',
    required=True
)
parser.add_argument(
    '--graphite-port',
    help='Port on the Graphite server listening for monitoring messages',
    action='store',
    type=int,
    required=True
)
parser.add_argument(
    '--buoy-id',
    help='',
    action='store',
    required=True
)
parser.add_argument(
    '--lat',
    help='',
    action='store',
    required=True
)
parser.add_argument(
    '--lon',
    help='',
    action='store',
    required=True
)

args = parser.parse_args()

timestamp = datetime.now().timestamp()

station_keeping = {
    'cpu': random.randrange(100 + 1),
    'moisture': random.randrange(10),
    'battery': 60,
    'lat': args.lat,
    'lon': args.lon
}

fluor_data = {"sensor_" + str(id): random.randrange(512, 768) for id in range(6)}


# Shape data into expected tuple shape for sending to Graphite
message_buffer = []

for (key, val) in station_keeping.items():
    message_buffer.append(
        (
            'buoy_monitor.' + args.buoy_id + '.station_keeping.' + key,
            (timestamp, val)
        )
    )

for (key, val) in fluor_data.items():
    message_buffer.append(
        (
            'buoy_monitor.' + args.buoy_id + '.fluorescence.' + key,
            (timestamp, val)
        )
    )

# Send data to Graphite
payload = pickle.dumps(message_buffer, protocol=2)
header = struct.pack("!L", len(payload))
message = header + payload

sock = socket.socket()
sock.connect((args.graphite_host, args.graphite_port))
sock.sendall(message)
sock.close()