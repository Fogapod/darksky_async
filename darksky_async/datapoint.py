from datetime import datetime

class DataPoint():
    # here we go
    __slots__ = (
        'apparentTemperature',
        'apparentTemperatureHigh',
        'apparentTemperatureHighTime',
        'apparentTemperatureLow',
        'apparentTemperatureLowTime',
        'apparentTemperatureMax',
        'apparentTemperatureMaxTime',
        'apparentTemperatureMin',
        'apparentTemperatureMinTime',
        'cloudCover',
        'dewPoint',
        'humidity',
        'icon',
        'moonPhase',
        'nearestStormBearing',
        'nearestStormDistance',
        'ozone',
        'precipAccumulation',
        'precipIntensity',
        'precipIntensityError',
        'precipIntensityMax',
        'precipIntensityMaxTime',
        'precipType',
        'precipProbability',
        'pressure',
        'summary',
        'sunriseTime',
        'sunsetTime',
        'temperature',
        'temperatureHigh',
        'temperatureHighTime',
        'temperatureLow',
        'temperatureLowTime',
        'temperatureMax',
        'temperatureMaxTime',
        'temperatureMin',
        'temperatureMinTime',
        'time',
        'uvIndex',
        'uvIndexTime',
        'visibility',
        'windBearing',
        'windGust',
        'windGustTime',
        'windSpeed'
    )
    def __init__(self, **optional_params):
        for key, value in optional_params.items():
            if key.lower().endswith('time'):
                value = datetime.utcfromtimestamp(value)
            setattr(self, key, value)
