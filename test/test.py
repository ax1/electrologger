from src.probe import *


def test_probe():
    probe = Probe('power')


def test_oscillator():
    curve = Linear_oscillator(100)
    for r in range(1000):
        print(str(curve.next())+" ", end='')
    print()


test_oscillator()
