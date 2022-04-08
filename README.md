# Electrologger

Data log generator for emulating EV charge events.

Logs created in plain text and homomorphically encrypted externally.
Those encrypted logs are then computed homomorphically and detect anomalies on data.

## Installation

```
git clone https://github.com/ax1/electrologger.git
pip install numpy
```
## Usage

### Configuration

A `config.json` file is created the first time. Tune the values if needed.

### Run

```sh
python3 main.py # display help with commands
# python3 main.py run # generate log files every 10 minutes
# python3 main.py all # generate a full dataset of logs and stop
```

Files are stored in the `log/` folder. The folder can be read and deleted in run-time (files are generated when buffer is full, and the log folder is recreated if not exists).

Debug: `python3 debug.py`

Test: `python3 test.py`


## Logs format

````
1648206486787, 10:00AM, boiler-672, power, 100, 50, NA, NA
1648206498221, 10:01AM, PC-15542,   fail,  NA,  NA, ERR2, 8
````
Two kind of sensors:
- **Gaussian random walk**. The timeline behaves like a periodic continuous sensor with noise.
- **Gaussian random jump**. The timeline is fully random. The sum of random values still following a normal distribution. 

Three kind of data;
- NORMAL data, sensors producing data.
- ANOMALY data, sensors producing data not following historical behaviour.
- ERROR events, atomic events producing "alert" error codes.

Line format

``` 
timestamp | date | source(id) | type(parameter) | [val_1, val_2] OR [subtype, val_1]
``` 

## Inserting intelligence-based anomalies

( This information is only available to project partners for now)

# License

[MIT](LICENSE.txt)

# Acknowledgements

This repository is part of the [ELECTRON "rEsilient and seLf-healed EleCTRical pOwer Nanogrid"](https://electron-project.eu/) project. This project has received funding from the European Union’s Horizon 2020 research and innovation programme under Grant Agreement No. 101021937. 