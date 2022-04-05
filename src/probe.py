import numpy as np
import random


def Probe(type):
    if type == 'power':
        return Probe_power(type, 1, 20)
    elif type == 'power_sub':
        return Probe_power(type, 2, 5)
    else:
        raise Exception(f'Sensor type "{type}" not implemented')


class Probe_gaussian:
    '''
    dist = the normalized distribution function [0,1]
    x = dist()
    f(x) = ax + b , f(x) is the linear translation to realistic values
    '''

    def __init__(self, _type):
        self.type = _type
        self.curve = None
        self.size = 2000
        self.dist = np.random.default_rng().normal(0, 1, self.size)
        self.a = 1
        self.b = 0
        self._oscillator = Linear_oscillator(self.size)
        self.anomaly = None

    def next(self):
        '''
        The curve must follow
         - time perspective (frontal view): walk on the points, when end path, walk backwards (sinusoidal-like graph)
         - time stripped (side view): the count for all walked points must show the same curve (e.g.:a gaussian distribution)
        '''
        point = self._oscillator.next()
        x = self.curve[point]

        # if anomaly is isalive, change the value
        if self.anomaly != None:
            if self.anomaly.is_alive() == False:
                self.anomaly = None  # destroy anomaly
            else:
                x = self.anomaly.a*x+self.anomaly.b
        return self.f(x)
        # use this instead if only rand values are required (only static normal, no time-based prediction)
        # return self.f(np.random.choice(self.dist))

    def f(self, x):
        return self.a*x+self.b


class Probe_power (Probe_gaussian):

    def __init__(self, _type, a, b):
        super().__init__(_type)
        self.a = a
        self.b = b
        self.curve = np.sort(self.dist)
        # print(self.curve)


class Probe_timeseries_arima:

    def __init__(self, _type, a, b):
        # TODO (see the test folder)
        self.a = a
        self.b = b
        self.curve = np.sort(self.dist)
        self.anomaly = None
        # print(self.curve)


class Linear_oscillator:
    '''
    A periodic function, with LINEAR weight, and with random steps to behave as real and not simulated
    The calculated mean is not n/2 (as should expect) due to oscillator rebounds, but enough near for our purposes
    Expected V/t chart: triangle, linear, mean n/2, period n
    '''

    def __init__(self, size):
        self.r = round(size/2)  # start from mean
        self.size = size
        self.forward = True
        self.step = round(size/10)

    def next(self):
        # s = 1 if self.forward else -1  # this is the "pure" function to compare with
        sign = random.choice([-1, 1])
        bias = 1 if self.forward else -1
        #s = random.randint(1, self.step) if self.forward else -random.randint(1, self.step)
        s = sign*random.randint(1, self.step)+bias
        self.r = self.r+s
        if self.r >= self.size:
            self.forward = False
            self.r = self.r-s
        elif self.r <= 0:
            self.forward = True
            self.r = self.r-s
        return self.r

# test linear oscillator
# curve = Linear_oscillator(100)
# for r in range(1000):
#     print(str(curve.next())+" ", end='')
# print()
