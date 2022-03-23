# Generate a file every X seconds
# Create a set of rows containing plain data, then save to folder

# period_file,number_rows, file_name?, folder

import json
import os


def start():
    config = json.loads(os.environ.get('config'))
    print(config)
