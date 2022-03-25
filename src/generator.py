# Generate a file every X seconds
# Create a set of rows containing plain data, then save to folder

# period_file,number_rows, file_name?, folder

import json
import os
import time
from .Sensor import Sensor


def start():
    config = json.loads(os.environ.get('config'))
    tick = config['interval_millis']/1000
    sensors = generate_sensors(config)
    while(True):
        time.sleep(tick)
        next_tick(sensors)
        collect(sensors)


def generate_sensors(config):
    sensors = []
    definitions = config['sensors']
    for definition in definitions:
        sensors.append(Sensor(definition))
    return sensors


def next_tick(sensors):
    for sensor in sensors:
        sensor.run()


def collect(sensors):
    print('')
    for sensor in sensors:
        print(str(sensor))
