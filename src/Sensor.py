import time
from .util import now


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
        self.value = 0
        print(definition)

    def run(self):
        self.value = self.value+1
        self.timestamp = now()

    def __str__(self):
        human_time = time.strftime('%H:%M%p')  # '%H:%M%p %Z on %b %d, %Y'
        return f'{self.timestamp}, {human_time}, {self.device}, {self.type}, {self.value}'
