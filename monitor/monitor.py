from datetime import datetime
import random


timestamp = datetime.now().timestamp()

station_keeping_data = {
    'cpu': random.randrange(100 + 1),
    'moisture': random.randrange(10),
    'battery': 60
}

fluor_data = {"sensor_" + str(id): random.randrange(512, 768) for id in range(6)}

print('end of program')
