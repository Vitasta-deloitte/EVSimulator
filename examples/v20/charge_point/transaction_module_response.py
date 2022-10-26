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
    @on('GetTransactionStatus')
    def on_get_transaction_status(self, transaction_id):
        print("receive for a Transaction status")
        return call_result.GetTransactionStatusPayload(
        messages_in_queue= True
        )
    @on('RequestStartTransaction')
    def on_start_transaction(self,id_token,remote_start_id):
        print("receive for a Transaction")
        return call_result.RequestStartTransactionPayload(
            status= "Accepted",
            status_info = None,
            transaction_id =None
        )
    @on('TransactionEvent')
    def on_transaction_event(self,event_type,timestamp,trigger_reason,seq_no,transaction_info):
        print("receive for a Transaction Event")
        return call_result.TransactionEventPayload(
            total_cost= None,
            charging_priority = None,
            id_token_info= None,
            updated_personal_message = None
        )
    @on('RequestStopTransaction')
    def on_stop_transaction(self,transaction_id):
        print("receive for stopping Transaction")
        return call_result.RequestStopTransactionPayload(
        status= "Accepted"
        )