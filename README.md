## DarkSky - Async Python 3 Library
Designed with native asyncio support, this libary is better suited to those who need better concurrency support than running requests inside `run_in_executor`.

## Usage
You can use several methods to use this libary, including directly calling the helper function `forecast`. This offers no setup but is significantly slower due to the need to create the client in the background everytime. Its better to just create the client and save it to a variable than using this function.

**Client example**:
```py
import asyncio
import darksky_async

client = darksky_async.Client("YOUR_DARKSKY_API_KEY_HERE")
loop = asyncio.get_event_loop()

loop.run_until_complete(client.forecast(latitude, longitude))
```

**Quick example**:
```py
import asyncio
import darksky_async

async def example_function():
  result = await darksky_async.forecast(key, latitude, longitude)
  
loop = asyncio.get_event_loop()

loop.run_until_complete(example_function())
```
