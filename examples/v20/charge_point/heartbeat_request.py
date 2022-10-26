import asyncio
from doctest import master
import logging
from urllib import request
from datetime import datetime
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
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result
logging.basicConfig(level=logging.INFO)
class ChargePoint(cp):

    async def send_heartbeat(self, interval):
        request = call.HeartbeatPayload()
        while True:
            await self.call(request)
            await asyncio.sleep(interval)

    async def send_notification_request(self):
        # Available ,Occupied ,Reserved, Unavailable, Faulted
        request = call.StatusNotificationPayload(timestamp= datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", connector_status= "Available", evse_id= 1, connector_id= 1)
        response = await self.call(request)