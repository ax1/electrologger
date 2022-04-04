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


def test_sensor():
    sensor = Sensor('boiler-672,power,normal')
    arr = []
    timestamp = 0
    for r in range(2000):
        timestamp += 1
        sensor.run(timestamp)
        arr.append(sensor.value1)
    narr = np.array(arr)

    #plt.hist(narr, bins=50, density=True)
    (n, bins) = np.histogram(narr, bins=10, density=True)
    fig, axd = plt.subplot_mosaic(
        [['1', '2'], ['3', '3']], layout='constrained')
    axd['1'].plot(.5 * (bins[1:] + bins[:-1]), n)
    axd['3'].plot(narr)
    plt.show()


def test_plot():
    fig, axd = plt.subplot_mosaic(
        [['1', '2'], ['3', '2']], layout='constrained')
    axd['1'].set_title('1')
    plt.show()


# test_oscillator()
test_sensor()
# test_plot()
