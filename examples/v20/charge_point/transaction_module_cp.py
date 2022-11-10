import logging

import sys 
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):

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


    @on('GetTransactionStatus')
    def on_get_transaction_status(self, transaction_id):
        print("Receive for Status of Transaction")
        return call_result.GetTransactionStatusPayload(
        messages_in_queue= True
        )
    