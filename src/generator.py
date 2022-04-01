# Generate a file every X seconds
# Create a set of rows containing plain data, then save to folder

# period_file,number_rows, file_name?, folder

import json
import os
import time
from src.sensor import Sensor
from src.util import now


def start():
    config = json.loads(os.environ.get('config'))
    millis = speed(config['speed'])
    sensors = generate_sensors(config)
    timestamp = now()
    counter = 0
    while(True):
        # time.sleep(1)
        timestamp = timestamp+millis
        next_tick(sensors, timestamp)
        collect(sensors)
        counter = counter+len(sensors)
        if counter > 10000:
            # generate log file
            print('Preparing another log file in 10 minutes...')
            time.sleep(10*60*1000)  # 10 min
            counter = 0


def generate_sensors(config):
    sensors = []
    definitions = config['sensors']
    for definition in definitions:
        try:
            sensors.append(Sensor(definition))
        except Exception as e:
            print(e)
    return sensors


def next_tick(sensors, timestamp):
    for sensor in sensors:
        sensor.run(timestamp)


def collect(sensors):
    for sensor in sensors:
        print(sensor)  # str(sensor)


def speed(definition):
    '''
    Speed of tick life in millis
    '''
    val = float(definition[0:-1])
    type = definition[-1]
    mult = 1
    if type == 's':
        mult = 1
    elif type == 'm':
        mult = 60
    else:
        raise f'Error in speed config ({definition}). Examples:0.01s (10 millis),1m (1 minute), etc'
    speed = val*mult
    return int(speed*1000)
