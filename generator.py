# Generate a file every X seconds
# Create a set of rows containing plain data, then save to folder

# period_file,number_rows, file_name?, folder

import json
import os
import time


def start():
    config = json.loads(os.environ.get('config'))
    T = config['interval_millis']/1000
    while(True):
        time.sleep(T)
        generate_rows()


def generate_devices():


def generate_event():
    r1 = generate_power_normal()
    #r2 = generate_power_anomaly()
    r3 = generate_fail_normal()
    #r4 = generate_fail_anomaly()


def generate_power_normal():
    print('aa')
