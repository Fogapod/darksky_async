
from .datablock import DataBlock
from .datapoint import DataPoint

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
        'timezone'
    )
    def __init__(self, latitude, longitude, timezone, **optional_params):
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        for key, value in optional_params.items():
            if key in IS_DATABLOCK:
                setattr(self, key, DataBlock(**value))
            elif key == 'currently':
                setattr(self, key, DataPoint(**value))
            elif key == 'alerts':
                # handle alerts array
                pass
            elif key == 'flags':
                # handle flags array
                pass
