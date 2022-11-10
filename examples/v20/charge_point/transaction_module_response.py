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
    
    #Extra
    async def send_start_transaction(self):
        request = call.RequestStartTransactionPayload(
            id_token={ "idToken": "001681020001", "type": "Central" },
            remote_start_id=2,
            )
        response = await self.call(request)
        print("Call for starting Transaction")
        print(response)

    #Extra
    async def send_stop_transaction(self):
        request = call.RequestStopTransactionPayload(
            transaction_id = "1")
        response = await self.call(request)
        print("Call for stopping Transaction")
        print(response)

    async def send_transaction_event(self,event_type,timestamp,trigger_reason,seq_no,transaction_info,number_of_phases_used,cable_max_current,reservation_id,evse,id_token,offline,meter_value):
        request = call.TransactionEventPayload(
            event_type= event_type,
            timestamp= timestamp,
            trigger_reason = trigger_reason,
            seq_no = seq_no,
            transaction_info= transaction_info,
            number_of_phases_used=number_of_phases_used,
            cable_max_current=cable_max_current,
            reservation_id=reservation_id,
            evse=evse,
            id_token=id_token,
            offline=offline,
            meter_value=meter_value
            )
        response = await self.call(request)
        print("Call for Event Transaction")
        print(response)
        # return call.TransactionEventPayload.event_type
        # return "Started"


    @on('GetTransactionStatus')
    def on_get_transaction_status(self, transaction_id):
        print("Receive for Status of Transaction")
        return call_result.GetTransactionStatusPayload(
        messages_in_queue= True
        )
    