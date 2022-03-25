from time import time


def now():
    '''
    The easiest way to get epoch:
     - in milliseconds 
     - as Integer

     This epoch is 100% equivalent to timestamp in other laguages
    '''
    return round(time() * 1000)
