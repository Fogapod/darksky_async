__author__ = 'Cerulean'
import unittest
from aiounittest import async_test
import asyncio

import darksky_async
from darksky_async.forecast import Forecast

loop = asyncio.get_event_loop()

class DarkSkyTest(unittest.TestCase):
    def setUp(self):
        self.loop = loop
        self.client = darksky_async.Client('<your darksky key>', loop=self.loop)
        
    @async_test(loop=loop)
    async def test_forecast(self):
        """
        This tests the forecast function.
        This will exclude minutely and use the SI units
        """
        result = await self.client.forecast(42.3601, -71.0589, exclude=['minutely'], units='uk2') # LA, USA

        self.assertIsNotNone(result, msg="Check for existance of the forecast object")
        self.assertIsInstance(result, Forecast, msg="Verify if the object is of type Forecast")

        # now we test if the minutely block is None
        self.assertFalse(hasattr(result, 'minutely'))

        # verify if the units are "uk2"
        self.assertEqual(result.flags.units, 'uk2')

if __name__ == '__main__':
    unittest.main()