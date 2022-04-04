import time


def now():
    '''
    The easiest way to get epoch:
     - in milliseconds 
     - as Integer

     This epoch is 100% equivalent to timestamp in other laguages
    '''
    return round(time.time() * 1000)


def sdate(timestamp):
    '''
    Note: timestamp is epoch time in millis (not in micros)
    '''
    return time.strftime(
        '%Y/%m/%d %H:%M:%S', time.localtime(timestamp/1000))
