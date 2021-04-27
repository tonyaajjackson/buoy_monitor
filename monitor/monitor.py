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

args = parser.parse_args()

message_buffer = []
timestamp = datetime.now().timestamp()

# Shape data into expected tuple shape for sending to Graphite
message_buffer = message_buffer + \
    [
        ('station_keeping.cpu', (timestamp, random.randrange(100 + 1))),
        ('station_keeping.moisture', (timestamp, random.randrange(10))),
        ('station_keeping.battery', (timestamp, 60))
    ]

message_buffer = message_buffer + \
    [("fluorescence.sensor_" + str(id), (timestamp, random.randrange(512, 768))) for id in range(6)]

# Send data to Graphite
payload = pickle.dumps(message_buffer, protocol=2)
header = struct.pack("!L", len(payload))
message = header + payload

sock = socket.socket()
sock.connect((args.graphite_host, args.graphite_port))
sock.sendall(message)
sock.close()