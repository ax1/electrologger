import time


class Sensor:

    '''
    Sensors are elements that produce data.
    They usually belong to one device,
    but the behaviour (state) for data generation is here.
    '''

    def __init__(self, definition):
        arr = definition.split(',')
        self.device = arr[0]
        self.source = arr[0]
        self.type = arr[0]
        self.anomaly = arr[0]
        self.timestamp = round(time.time() * 1000)
        print(definition)

    def run(self):
        return 'create line'
