# Electrologger

Data log generator for emulating EV charge events.

Logs created in plain text and homomorphically encrypted externally.
Those encrypted logs are then computed homomorphically and detect anomalies on data.

## Usage

Configuration: A `shared/config.json` file is created the first time. Tune the values if needed.

Run: `python3 main.py` . The app creates ASAP a valid log file, then wait 10 min to create another one. So 2 options: run/stop several times the app to get many files, or leave the app running to create one file every 10 minutes 

## Test (for developers)

Run `python3 -m test.test`

## Requirements

### Logs format

````
1648206486787, 10:00AM, boiler-672, power, 100, 50, NA, NA
1648206498221, 10:01AM, PC-15542,   fail,  NA,  NA, ERR2, 8
````

Line format

``` 
timestamp | date | source(id) | type(parameter) | [val_1, val_2] OR [subtype, val_1]
``` 

## Inserting intelligence-based anomalies

(non-public data for now)
