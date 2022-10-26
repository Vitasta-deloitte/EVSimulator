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

    async def get_transaction_status(self):
        request = call.GetTransactionStatusPayload(
            transaction_id="2")

        response = await self.call(request)
        print("calll for a transaction status")
        print(response)
        # if response.status == 'Accepted':
            # print("reservation is  booked" , response.status_info)
    async def send_start_transaction(self):
        request = call.RequestStartTransactionPayload(
            id_token={ "idToken": "001681020001", "type": "Central" },
            remote_start_id=2,
            # evse_id= None, 
            # group_id_token= None,
            # charging_profile=None
            )

        response = await self.call(request)
        print("calll for a start Transaction")
        print(response)
    async def send_transaction_event(self):
        request = call.TransactionEventPayload(
            event_type= "Started",
            timestamp= "1666775586",
            trigger_reason = "CablePluggedIn",
            seq_no = 111,
            transaction_info= {"transactionId":"1234"}
            # meter_value = None,
            # offline= None,
            # number_of_phases_used = None,
            # cable_max_current = None,
            # reservation_id = None,
            # evse=None,
            # id_token=None,
            # id_token={ "idToken": "001681020001", "type": "Central" },
            # remote_start_id=2,
            # evse_id= None, 
            # group_id_token= None,
            # charging_profile=None
            )

        response = await self.call(request)
        print("calll for a Transaction Event")
        print(response)
    async def send_stop_transaction(self):
        request = call.RequestStopTransactionPayload(
            transaction_id = "1")
        response = await self.call(request)
        print("Transaction Stop !!!")
        print(response)
    
