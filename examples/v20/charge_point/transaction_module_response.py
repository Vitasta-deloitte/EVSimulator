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
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):
 
    async def send_start_transaction(self):
        request = call.RequestStartTransactionPayload(
            id_token={ "idToken": "001681020001", "type": "Central" },
            remote_start_id=2,
            )
        response = await self.call(request)
        print("Call for starting Transaction")
        print(response)

    async def send_stop_transaction(self):
        request = call.RequestStopTransactionPayload(
            transaction_id = "1")
        response = await self.call(request)
        print("Call for stopping Transaction")
        print(response)

    async def send_transaction_event(self, event_type,timestamp,trigger_reason,seq_no,transactionId):
        request = call.TransactionEventPayload(
            event_type= event_type,
            timestamp= timestamp,
            trigger_reason = trigger_reason,
            seq_no = seq_no,
            transaction_info= {"transactionId":transactionId}
            )
        response = await self.call(request)
        print("Call for Event Transaction")
        print(response)

    @on('GetTransactionStatus')
    def on_get_transaction_status(self, transaction_id):
        print("Receive for Status of Transaction")
        return call_result.GetTransactionStatusPayload(
        messages_in_queue= True
        )
    