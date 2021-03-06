## DarkSky - Async Python 3 Library
Designed with native asyncio support, this libary is better suited to those who need better concurrency support than running requests inside `run_in_executor`.
As this is an asyncio based libary, we do not plan to support Python 2. The minimum Python version needed is 3.5, [you can download it here](https://www.python.org/downloads/)

## Usage
You can use several methods to use this libary, including directly calling the helper function `forecast`. This offers no setup but is significantly slower due to the need to create the client in the background everytime. Its better to just create the client and save it to a variable than using this function.

**Client example**:
```py
import asyncio
import darksky_async

async def main():
    client = darksky_async.Client("DarkSky key goes here")

    weather = await client.forecast(
        37.8267, # latitude
        -122.4233 # longitude
    )
    print(weather.currently)
    print(weather.daily.data[0].timeLocal)
    # time-based items have a local time
    # version that allows you to convert between the two easily


client = darksky_async.Client("YOUR_DARKSKY_API_KEY_HERE")
loop = asyncio.get_event_loop()

loop.run_until_complete(client.forecast(latitude, longitude))
```

**Quick example**:
```py
import asyncio
import darksky_async

async def example_function():
  result = await darksky_async.forecast(key, latitude, longitude, exclude=['minutely', 'hourly'], units='si')
  
loop = asyncio.get_event_loop()

loop.run_until_complete(example_function())
```

## Extra features
All time-based entries for DataPoint have a local version as well. Thanks to PyTz we can convert the datetime to the local time for quicker and easier access of time.
All you need to do to access this local time is append `Local` to any time-based datapoint:
```py
weather = await client.forecast(37.8267, -122.4233)

utc_time = weather.daily.data[0].sunriseTime
>>> '2pm' # Abbreviated for simplicity
local = weather.daily.data[0].sunriseTimeLocal
>>> '6am' # -8 hours behind UTC, this time is accurate for Los Angeles, USA
```

This libary also keeps a track of how much is due. When running a forecast, you can check the current amount due by doing:
```py
weather = await client.forecast(lat, lon)
print(weather.total_due)
```
The returned amount will be in dollars as per the terms of service [here](https://darksky.net/dev/docs/terms#payments)
As a note: this is only the daily cost. We cannot track the *actual* amount owed due to DarkSky having that information on lock down.