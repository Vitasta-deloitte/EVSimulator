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
    # @on('RequestStartTransaction')
    # def on_start_transaction(self,id_token,remote_start_id):
    #     print("Receive for Starting Transaction")
    #     return call_result.RequestStartTransactionPayload(
    #         status= "Accepted",
    #         status_info = None,
    #         transaction_id =None
    #     )

    async def send_stop_transaction(self):
        request = call.RequestStopTransactionPayload(
            transaction_id = "1")
        response = await self.call(request)
        print("Call for stopping Transaction")
        print(response)
    # @on('RequestStopTransaction')
    # def on_stop_transaction(self,transaction_id):
    #     print("Receive for stopping Transaction")
    #     return call_result.RequestStopTransactionPayload(
    #     status= "Accepted"
    #     )

    async def send_transaction_event(self):
        request = call.TransactionEventPayload(
            event_type= "Started",
            timestamp= "1666775586",
            trigger_reason = "CablePluggedIn",
            seq_no = 111,
            transaction_info= {"transactionId":"1234"}
            )
        response = await self.call(request)
        print("Call for Event Transaction")
        print(response)
        
    # @on('TransactionEvent')
    # def on_transaction_event(self,event_type,timestamp,trigger_reason,seq_no,transaction_info):
    #     print("Receive for a Event Transaction")
    #     return call_result.TransactionEventPayload(
    #         total_cost= None,
    #         charging_priority = None,
    #         id_token_info= None,
    #         updated_personal_message = None
    #     )


    @on('GetTransactionStatus')
    def on_get_transaction_status(self, transaction_id):
        print("Receive for Status of Transaction")
        return call_result.GetTransactionStatusPayload(
        messages_in_queue= True
        )
    