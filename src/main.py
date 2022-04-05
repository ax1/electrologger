import inspect
import os
from src.generator import start


def main():
    loadConfigFile()


def loadConfigFile():
    data = None
    path = 'shared/config/config.json'
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
    "rows_file": 10000,
    "anomalies":["normal","anomaly_sigma"],
    "sensors": [
        "boiler-672,power,normal",
        "laptop-33,power,anomaly_sigma",
        "laptop-35,temp,normal"
    ]
}
'''
