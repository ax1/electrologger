# Generate a file every X seconds
# Create a set of rows containing plain data, then save to folder

# period_file,number_rows, file_name?, folder

import json
import os
import time
from src.sensor import Sensor
from src.util import now, sdate
import re
import random


def start():
    config = json.loads(os.environ.get('config'))
    elapsed = speed(config['speed'])
    max_rows = config['rows']
    sensors = generate_sensors(config)
    timestamp = now()
    counter = 0
    rows = []
    filename = None
    folder = 'log/'
    while(True):
        if(filename == None):
            os.makedirs(os.path.dirname(folder), exist_ok=True)
            filename = re.sub('/|\:', '', sdate(timestamp)+'.csv')
            filename = filename.replace(' ', '_')
        # time.sleep(1)
        timestamp = timestamp+elapsed
        next_tick(sensors, timestamp)
        collect(sensors, rows)
        counter = counter+len(sensors)
        if counter >= max_rows:
            # generate log file
            f = open(folder+filename, 'w')
            f.write('\n'.join(rows))
            print(f'Created {filename} file')
            rows = []
            filename = None
            print('Preparing another log file in 10 minutes...')
            time.sleep(10*60)  # 10 min
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
        if generate_anomaly() == True:
            sensor.generate_anomaly(timestamp)
        sensor.run(timestamp)


def collect(sensors, rows):
    for sensor in sensors:
        s = str(sensor)
        if generate_error() == True:
            s = sensor.create_error()
        if s != '':
            rows.append(s)


def generate_error():
    val = random.randint(-1, 2000)  # 2000 = 10 errors-events/file10K
    return True if val < 0 else False


def generate_anomaly():
    # 5000 = 1 anomalies/file10K = for 5 sensors= 1 file with sensor-anomaly in every 5 files
    val = random.randint(-1, 10000)
    return True if val < 0 else False


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
