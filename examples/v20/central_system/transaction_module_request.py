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


    @on('RequestStartTransaction')
    def on_transaction_start_transaction(self,id_token,remote_start_id):
        print("Receive for Starting Transaction")
        return call_result.RequestStartTransactionPayload(
            status= "Accepted",
            transaction_id ="1",
            status_info = None
        )

    @on('RequestStopTransaction')
    def on_transaction_stop_transaction(self,transaction_id):
        print("Receive for stopping Transaction")
        return call_result.RequestStopTransactionPayload(
        status= "Accepted"
        )
    
    @on('TransactionEvent')
    def on_transaction_transaction_event(self,event_type,timestamp,trigger_reason,seq_no,transaction_info,number_of_phases_used,cable_max_current,reservation_id,evse,id_token,offline,meter_value):
        print("Receive for a Event Transaction")
        total_cost= None
        charging_priority = None
        id_token_info= None
        updated_personal_message = None
        # if event_type=="Started" and trigger_reason=="EVDetected":
        #     total_cost=1
        # return call_result.TransactionEventPayload(
        #     total_cost= total_cost,
        #     charging_priority = charging_priority,
        #     id_token_info= id_token_info,
        #     updated_personal_message = updated_personal_message
        # )
        # if event_type=="Started" and trigger_reason=="EVDetected" :
        #     pass
        # if event_type=="Started" and trigger_reason=="CablePluggedIn" and transaction_info["chargingState"]=="EVConnected":
        #     pass
        # if event_type=="Started" and trigger_reason=="Authorized":
        #     # id_token_info = {"status":"Accepted"}
        #     pass
        # if event_type=="Started" and trigger_reason=="SignedDataReceived":
        #     pass
        # if event_type=="Started" and trigger_reason=="ChargingStateChanged" and transaction_info["chargingState"]=="Charging":
        #     pass
        # print("+++++++++++++++++++++++++++++++++++",event_type, trigger_reason, transaction_info["charging_state"])
        # if event_type == "Started" and trigger_reason == "CablePluggedIn" and transaction_info["charging_state"] == "EVConnected":
        #     id_token_info={"status":"Accepted"}
        # else:
        #     id_token_info={"status":"Blocked"}
        # if event_type=="Started" and trigger_reason=="CablePluggedIn" and transaction_info["chargingState"]=="EVConnected":
        #     pass
        # if event_type=="Updated" and trigger_reason=="Authorized":
        #     pass
        # if event_type=="Updated" and trigger_reason=="ChargingStateChanged":
        #     pass
        # if event_type=="Ended" and trigger_reason == "EVConnectTimeout":
        #     pass
        return call_result.TransactionEventPayload(
            total_cost= total_cost,
            charging_priority = charging_priority,
            id_token_info= id_token_info,
            updated_personal_message = updated_personal_message
        )

    async def get_transaction_transaction_status(self):
        request = call.GetTransactionStatusPayload(
            transaction_id="2")
        response = await self.call(request)
        print("Call for status of transaction")
        print(response)

   
