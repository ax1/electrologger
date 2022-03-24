import time


class Sensor:

    '''
    Sensors are elements that produce data.
    They usually belong to one device,
    but the behaviour (state) for data generation is here.
    '''

    def __init__(self, source, type, anomaly) -> None:
        self.source = source
        self.type = type
        self.anomaly = anomaly
        self.timestamp = round(time.time() * 1000)

    def run(self):
        return 'create line'
