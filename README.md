# Electrologger

Data log generator for emulating EV charge events.

Logs created in plain text and homomorphically encrypted externally.
Those encrypted logs are then computed homomorphically and detect anomalies on data.

## Usage

Configuration: A `shared/config.json` file is created the first time. Tune the values if needed.

Run: `python3 main.py`

## Requirements

### Logs format

````
12345678, 10:00AM, boiler-672, power, 100, 50, NA,   NA
12345689, 10:01AM, PC-15542,   fail,  NA,  NA, ERR2, 8
````

Line format

``` 
timestamp | date | source(id) | type(parameter) | [val_1, val_2] OR [subtype, val_1]
``` 

## Inserting intelligence-based anomalies

(See IBM email)




