from mimetypes import init


class Device:
    '''
    A device is a bare collection of Sensor objects
    '''

    def __init__(self, definition):
        self.__definition = definition
        print('New device: '+definition)
