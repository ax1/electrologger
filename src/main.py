import inspect
import os
from src.generator import start


def main():
    loadConfigFile()


def loadConfigFile():
    data = None
    path = 'config.json'
    try:
        f = open(path, 'r')
        data = f.read()
    except FileNotFoundError:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        data = inspect.cleandoc(template)
        f = open(path, 'w')
        f.write(data)

    os.environ['config'] = data
    start()


template = '''
{
    "speed": "1s",
    "rows": 10000,
    "sensors": [
        "boiler-672,power,normal",
        "laptop-33,power,anomaly_sigma",
        "laptop-35,temp,normal"
    ],
    "help": {
        "speed": "1s 5s 1m 15m 0.1s...etc",
        "rows": "number of total rows per file",
        "sensors": "format: device_id,sensor_type,anomaly_type where sensor_type=power,temp,etc and anomaly_type=normal(no anomaly),anomaly_sigma, etc.."
    }
}
'''
