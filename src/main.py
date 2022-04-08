import inspect
import os
import sys
from src.generator import start
import test.test as test

YELLOW = '\x1b[33;20m'
RESET = '\x1b[0m'


def main():
    loadConfigFile()
    help = f'''Generate log files with different anomalies.

Usage:
    {YELLOW}python3 main [option]{RESET}
    (a config.json file is created the first time. Add more sensors in that file).

option: 
    {YELLOW}run:{RESET} generate ONE log file, and contiuously, another file every 10 minutes
    {YELLOW}all:{RESET} generate ALL log files in one round and stop
    {YELLOW}test:{RESET} check if simulated sensors follow predictable behaviour
    {YELLOW}help:{RESET} display the options 
    '''
    option = None if len(sys.argv) < 2 else sys.argv[1]
    if option == None or option == 'help':
        return print(help)
    elif option == 'test':
        return test.main()
    elif option == 'run':
        return start(600)
    elif option == 'all':
        return start(0)
    else:
        raise (f'ERROR: option: {option} is not available')


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


template = '''
{
    "speed": "1s",
    "rows": 10000,
    "sensors": [
        "boiler-672,power,normal",
        "laptop-33,power,anomaly_sigma",
        "laptop-35,temp,normal",
        "chargeEV-A1,duration,anomaly_sigma",
        "chargeEV-A2,duration,anomaly_mean"
    ],
    "help": {
        "speed": "1s 5s 1m 15m 0.1s...etc",
        "rows": "number of total rows per file",
        "sensors": "format: device_id,sensor_type,anomaly_type where sensor_type=power,temp,etc and anomaly_type=normal(no anomaly),anomaly_sigma, etc.."
    }
}
'''
