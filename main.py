import inspect
import os
import generator


def main():
    if __name__ == "__main__":
        loadConfigFile()


def loadConfigFile():
    data = None
    path = 'shared/config.json'
    try:
        f = open(path, 'r')
        data = f.read()
    except FileNotFoundError:
        data = inspect.cleandoc(template)
        f = open(path, 'w')
        f.write(data)

    os.environ['config'] = data
    generator.start()


template = '''
{
    "interval_millis": 6,
    "rows_file": 10000,
    "sensors": [
        "boiler-672,power,normal",
        "PC-15542,fail,anomaly_1",
        "laptop-33,temp,anomaly_2",
        "laptop-33,fail,anomaly_1",
        "laptop-35,temp,normal"
    ]
}
'''

main()
