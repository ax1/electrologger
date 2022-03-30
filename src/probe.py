import numpy as np
import random


def Probe(type):
    if type == 'power':
        return Probe_power(type)
    else:
        raise Exception(f'Sensor type "{type}" not implemented')


class Probe_generic:
    '''
    dist = the normalized distribution function [0,1]
    x = dist()
    f(x) = ax + b , f(x) is the linear translation to realistic values
    '''

    def __init__(self, type):
        self.type = type
        self.curve = None
        self.size = 1000
        self._oscillator = Linear_oscillator(self.size)

    def next(self):
        return self.f(np.random.choice(self.dist))

    def f(self, x):
        return round(self.a*x+self.b)


class Probe_power (Probe_generic):

    def __init__(self, type):
        super(type)
        self.dist = np.random.default_rng().normal(0, 3, self.size)
        self.a = 1
        self.x = None
        self.curve = np.sort(self.dist)

    def next(self, x):
        '''
        The curve must follow
         - time perspective (frontal view): walk on the points, when end path, walk backwards (sinusoidal-like graph)
         - time stripped (side view): the count for all walked points must show the same curve (e.g.:a gaussian distribution)
        '''
        return self.curve[self._oscillator.next()]


class Linear_oscillator:
    '''
    A periodic function, with LINEAR weight, and with random steps to behave as real and not simulated
    The calculated mean is not n/2 (as should expect) due to oscillator rebounds, but enough near for our purposes
    Expected V/t chart: triangle, linear, mean n/2, period n
    '''

    def __init__(self, size):
        self.r = 0
        self.size = size
        self.forward = True

    def next(self):
        # s=s+1 if self.forward else s=s+1 # this is the "pure" function
        s = random.randint(1, 9) if self.forward else -random.randint(1, 9)
        self.r = self.r+s
        if self.r >= self.size:
            self.forward = False
            return self.next()
        elif self.r <= 0:
            self.forward = True
            return self.next()
        else:
            return self.r

# test linear oscillator
# curve = Linear_oscillator(100)
# for r in range(1000):
#     print(str(curve.next())+" ", end='')
# print()
