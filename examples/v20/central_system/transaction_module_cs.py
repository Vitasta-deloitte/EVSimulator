import logging
import sys
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call_result , call;

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):

    
    @on('TransactionEvent')
    def on_transaction_transaction_event(self,event_type,timestamp,trigger_reason,seq_no,transaction_info,number_of_phases_used,cable_max_current,reservation_id,evse,id_token,offline,meter_value):
        print("Receive for a Event Transaction")
        total_cost= None
        charging_priority = None
        id_token_info= {"status":"Accepted"}
        updated_personal_message = None
        if event_type=="Started":
            if "stopped_reason" in transaction_info:
                updated_personal_message={"format":"UTF8","content":"Disconnected"}
                id_token_info= {"status":"Blocked"}
            if offline==True or id_token["id_token"]=="NoAuthorization":
                id_token_info= {"status":"Unknown"}
        if event_type=="Ended":
            id_token_info= {"status":"Blocked"}
            updated_personal_message={"format":"UTF8","content":"Transaction Ended"}

        return call_result.TransactionEventPayload(
            total_cost= total_cost,
            charging_priority = charging_priority,
            id_token_info= id_token_info,
            updated_personal_message = updated_personal_message
        )

    async def get_transaction_transaction_status(self, transaction_id):
        request = call.GetTransactionStatusPayload(
            transaction_id=transaction_id)
        response = await self.call(request)
        print("Call for status of transaction")
        print(response)

   
