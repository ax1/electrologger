from src.probe import *
from src.sensor import *
import matplotlib.pyplot as plt


def test_probe():
    probe = Probe('power')


def test_oscillator():
    curve = Linear_oscillator(100)
    for r in range(1000):
        print(str(curve.next())+" ", end='')
    print()


def testSensor():
    sensor = Sensor('boiler-672,power,normal')
    arr = []
    for r in range(1000):
        sensor.run()
        arr.append(sensor.value1)
    narr = np.array(arr)
    #plt.hist(narr, bins=50, density=True)
    (n, bins) = np.histogram(narr, bins=10, density=True)
    plt.plot(.5 * (bins[1:] + bins[:-1]), n)
    plt.show()


# test_oscillator()
testSensor()
