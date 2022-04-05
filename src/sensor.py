import imp
import time
from datetime import datetime
from .util import now
from .probe import Probe
import random


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
        # self.anomaly = Value(anomaly_type)
        print(definition)

    def run(self, timestamp):
        self.value1 = self.probe1.next()
        self.value2 = self.probe2.next()
        #self.timestamp = now()
        self.timestamp = timestamp

    def format(self, value):
        return "{:.2f}".format(value)

    def __str__(self):
        # when no values->no record
        if self.value1 == None and self.value2 == None:
            return ''
        # '%H:%M%p %Z on %b %d, %Y'
        human_time = time.strftime(
            '%I:%M:%S%p', time.localtime(self.timestamp/1000))
        value1 = self.format(self.value1)
        value2 = self.format(self.value2)
        return f'{self.timestamp}, {human_time}, {self.device}, {self.type}, {value1}, {value2}, NA, NA'

    def create_error(self):
        human_time = time.strftime(
            '%I:%M:%S%p', time.localtime(self.timestamp/1000))
        print(f'Creating FAIL in {self.device} at {human_time}')
        value1 = self.format(self.value1)
        value2 = self.format(self.value2)
        return f'{self.timestamp}, {human_time}, {self.device}, fail, NA, NA, ERR{random.randint(1, 10)}, {random.randint(1, 100)}'
