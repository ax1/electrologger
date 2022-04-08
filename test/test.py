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


def test_sensor(definition):
    sensor = Sensor(definition)
    arr = []
    timestamp = 0

    # pure data
    for r in range(2000):
        timestamp += 1
        sensor.run(timestamp)
        arr.append(sensor.value1)
    backup = np.array(arr)

    # if anomaly, add more data
    sensor.generate_anomaly(timestamp)
    for r in range(2000):
        timestamp += 1
        sensor.run(timestamp)
        arr.append(sensor.value1)

    # paint data
    narr = np.array(arr)
    (m, mb) = np.histogram(backup, bins=10, density=True)
    (n, bins) = np.histogram(narr, bins=10, density=True)
    fig, axd = plt.subplot_mosaic(
        [['a', 'b'], ['c', 'c']], layout='constrained')
    axd['a'].set_title('Original')
    axd['b'].set_title('Anomaly')
    axd['c'].set_title('Timeline')
    axd['a'].plot(.5 * (mb[1:] + mb[:-1]), m)
    axd['b'].plot(.5 * (bins[1:] + bins[:-1]), n)
    axd['c'].plot(narr)
    # = plt.get_current_fig_manager()
    # manager.full_screen_toggle()
    plt.show()


def test_plot():
    fig, axd = plt.subplot_mosaic(
        [['1', '2'], ['3', '2']], layout='constrained')
    axd['1'].set_title('1')
    plt.show()


def test_timeseries_arima():
    mu = 50
    phi1 = 0.6
    phi2 = -0.4
    M = mu/(1-phi1)
    N = 2**17
    errors = np.random.normal(0, 1, N)
    X = [M]
    for t in range(1, N):
        X.append(mu + phi1*X[t-1] + phi2*errors[t-1] + errors[t])
    plt.plot(X)
    plt.show()


def main():
    # test_oscillator()
    # test_sensor('boiler-672,power,normal')
    # test_sensor('chargeEV,duration,anomaly_sigma')
    test_sensor('chargeEV,duration,anomaly_mean')
    # test_plot()
    # test_timeseries_arima()
