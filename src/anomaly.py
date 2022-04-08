import random


class Anomaly:

    def __init__(self, type):
        self.counter = 0
        self.type = type
        self.life = random.randint(2000, 4000)
        # multiplier. Direct sigma change Eg: f(x)=2x+4 -> g(x)=(a*2)x+4
        self.a = 1
        # multiplier. mean deviation in number of sigmas  .Eg: f(x)=2x+4 -> g(x)=2x+4+(2*b)
        self.b = 0
        if(type == 'anomaly_sigma'):
            self.a = random.randint(2, 5)
        elif(type == 'anomaly_mean'):
            self.b = random.randint(4, 7)  # min mean deviation=4
        else:
            raise f'anomaly type "{type}" is not implemented'

    def is_alive(self):
        self.counter = self.counter+1
        return True if self.counter < self.life else False
