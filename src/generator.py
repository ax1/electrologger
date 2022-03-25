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
    return
    while(True):
        time.sleep(tick)
        next_tick()
        collect()


def generate_sensors(config):
    sensors = []
    definitions = config['sensors']
    for definition in definitions:
        sensors.append(Sensor(definition))
    return sensors


def next_tick():
    print('aa')
    #r1 = generate_power_normal()
    #r2 = generate_power_anomaly()
    #r3 = generate_fail_normal()
    #r4 = generate_fail_anomaly()


def collect():
    print('save to log file')
