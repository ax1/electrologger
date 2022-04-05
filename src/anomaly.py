import random


class Anomaly:

    def __init__(self, type):
        self.counter = 0
        self.type = type
        self.life = random.randint(20, 200)
        self.a = 1  # multiplier. Eg: f(x)=2x+4 -> g(x)=(sigma*2)x+4
        self.b = 0  # addition.Eg: f(x)=2x+4 -> g(x)=2x+mean*4
        if(type == 'anomaly_sigma'):
            self.a = 5
        else:
            raise f'anomaly type "{type}" is not implemented'

    def is_alive(self):
        self.counter = self.counter+1
        return True if self.counter < self.life else False
