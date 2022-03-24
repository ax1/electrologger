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
        data = inspect.cleandoc('''
        {
            "interval_millis": 6,
            "rows_file": 10000
        }
        ''')
        f = open(path, 'w')
        f.write(data)

    os.environ['config'] = data
    generator.start()


main()
