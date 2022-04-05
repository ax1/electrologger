import imp
import time
from datetime import datetime
from .util import now, htime
from .probe import Probe
import random
from .anomaly import Anomaly


class Sensor:

    '''
    Sensors are elements that produce data.
    They usually belong to a device,
    but the real behaviour is performed in the sensor.
    '''

    def __init__(self, definition):
        arr = definition.split(',')
        self.device = arr[0]
        self.type = arr[1]
        self.anomaly_type = arr[2]
        self.timestamp = now()
        self.probe1 = Probe(self.type)
        self.probe2 = Probe(self.type+'_sub')
        self.value1 = self.probe1.next()
        self.value2 = self.probe2.next()
        self.counter = 0
        print(definition)

    def run(self, timestamp):
        self.counter = self.counter+1
        self.value1 = self.probe1.next()
        self.value2 = self.probe2.next()
        self.timestamp = timestamp  # s elf.timestamp = now()

    def format(self, value):
        return "{:.2f}".format(value)

    def __str__(self):
        # when no values->no record
        if self.value1 == None and self.value2 == None:
            return ''
        human_time = htime(self.timestamp)
        value1 = self.format(self.value1)
        value2 = self.format(self.value2)
        return f'{self.timestamp}, {human_time}, {self.device}, {self.type}, {value1}, {value2}, NA, NA'

    def create_error(self):
        human_time = htime(self.timestamp)
        print(f'Creating FAIL in {self.device} at {human_time}')
        return f'{self.timestamp}, {human_time}, {self.device}, fail, NA, NA, ERR{random.randint(1, 10)}, {random.randint(1, 100)}'

    def generate_anomaly(self, timestamp):
        if(self.anomaly_type != 'normal'):
            human_time = htime(self.timestamp)
            print(
                f'Creating ANOMALY {self.anomaly_type} in {self.device} at {human_time}')
            self.probe1.anomaly = Anomaly(self.anomaly_type)
