# Electrologger

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Data log generator for emulating EV charge events. The logs contain normal data, from time to time, an anomaly is generated making the sensor to provide new data. This anomaly can be detected by using AI techniques. 

The logs are created in plain text. They will be homomorphically encrypted by an external agent to protect privacy on data. The encrypted logs are then computed to detect anomalies on data, without sharing the real values.

## Installation

> Note: Python3 is required

```
git clone https://github.com/ax1/electrologger.git
cd electrologger
pip install numpy matplotlib
```
## Usage

### Configuration

A `config.json` file will be created automatically the first time. Tune the values if needed.

### Run

```sh
python main.py # display help with commands
# python main.py run # generate log files every 10 minutes
# python main.py all # generate a full dataset of logs and stop
```

Files are stored in the `log/` folder. The folder can be read and deleted in run-time (files are generated when buffer is full, and the log folder is recreated if not exists).

Debug: `python debug.py`

Test: `python test.py`


## Logs format

````
1648206486787, 10:00AM, boiler-672, power, 100, 50, NA, NA
1648206498221, 10:01AM, PC-15542,   fail,  NA,  NA, ERR2, 8
````

Where line format is:
``` 
timestamp | date | source(id) | type(parameter) | [val_1, val_2] OR [subtype, val_1]
``` 

Two kinds of sensors:
- **Gaussian random walk**. The timeline behaves like a periodic continuous sensor with noise.
- **Gaussian random jump**. The timeline is fully random. The sum of random values still following a normal distribution. 

Three kinds of data:
- NORMAL data, sensors producing data.
- ANOMALY data, sensors producing data not following historical behaviour.
- ERROR events, atomic events producing "FAIL" error codes.



## Inserting intelligence-based anomalies

( This information is only available to project partners for now)

# Acknowledgements

This repository is part of the [ELECTRON "rEsilient and seLf-healed EleCTRical pOwer Nanogrid"](https://electron-project.eu/) project. This project has received funding from the European Union’s Horizon 2020 research and innovation programme under Grant Agreement No. 101021937. 
