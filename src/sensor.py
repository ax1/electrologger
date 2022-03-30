import time
from .util import now
from .probe import Probe


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
        self.probe = Probe(self.type)
        self.value = self.probe.next()
        # self.anomaly = Value(anomaly_type)
        print(definition)

    def run(self):
        self.value = self.probe.next()
        self.timestamp = now()

    def format(self, value):
        return "{:.2f}".format(value)

    def __str__(self):
        human_time = time.strftime('%H:%M%p')  # '%H:%M%p %Z on %b %d, %Y'
        value = self.format(self.value)
        return f'{self.timestamp}, {human_time}, {self.device}, {self.type}, {value}'
