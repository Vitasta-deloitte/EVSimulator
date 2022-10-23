import asyncio
import logging
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
from ocpp.v201 import call_result , call;

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):

    async def send_reservation(self):
        request = call.ReserveNowPayload(
            id= 0, 
            expiry_date_time= "12/8/2022",
            id_token={ "idToken": "001681020001", "type": "Central" },
            connector_type= "cCCS1", 
            evse_id= None, 
            group_id_token= None)

        response = await self.call(request)
        print("calll for a reservation")
        print(response)
        # if response.status == 'Accepted':
            # print("reservation is  booked" , response.status_info)