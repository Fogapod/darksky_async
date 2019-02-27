
from .datablock import DataBlock
from .datapoint import DataPoint
from .flag import Flags

IS_DATABLOCK = [
    'minutely',
    'hourly',
    'daily'
]

class Forecast():
    __slots__ = (
        'currently',
        'minutely',
        'hourly',
        'daily',
        'alerts',
        'flags',
        'latitude',
        'longitude',
        'timezone',
        'headers',
        'raw',
        '_state'
    )
    def __init__(self, state, headers, latitude, longitude, timezone, **optional_params):
        self._state = state

        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.headers = headers # unprocessed
        self.raw = optional_params
        self.raw['latitude'] = latitude
        self.raw['longitude'] = longitude
        self.raw['timezone'] = timezone
        
        for key, value in optional_params.items():
            if key in IS_DATABLOCK:
                setattr(self, key, DataBlock(**value))
            elif key == 'currently':
                setattr(self, key, DataPoint(**value))
            elif key == 'alerts':
                # handle alerts array
                pass
            elif key == 'flags':
                setattr(self, key, Flags(**value))
