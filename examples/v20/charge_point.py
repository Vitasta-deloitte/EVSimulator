import asyncio
from doctest import master
import logging

try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys
    sys.exit(1)

import sys 
sys.path.append('../../')
from ocpp.v201 import call
from ocpp.v201 import ChargePoint as cp

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):

    async def send_heartbeat(self, interval):
        
        request = call.HeartbeatPayload()

        while True:
            await self.call(request)
            await asyncio.sleep(interval)

    async def send_boot_notification(self):
        print("call to server")
        request = call.BootNotificationPayload(
                charging_station={
                    'model': 'Wallbox XYZ',
                    'vendor_name': 'anewone'
                },
                reason="PowerUp"
        )
        response = await self.call(request)

        if response.status == 'Accepted':
            print("Connected to central system.")
            # await self.send_heartbeat()
            await self.send_heartbeat(response.interval)


async def main():
    async with websockets.connect(
        'ws://localhost:9000/CP_1',
        subprotocols=['ocpp2.0']
    ) as ws:

        cp = ChargePoint('CP_231', ws)
        print("hit it", ws )
        print(type(ws))
        await asyncio.gather(cp.start(), cp.send_boot_notification())


if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
