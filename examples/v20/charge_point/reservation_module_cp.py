import logging
import sys 
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result
logging.basicConfig(level=logging.INFO)
class ChargePoint(cp):

    @on('ReserveNow')
    def on_reservation(self , id , expiry_date_time, id_token,connector_type,evse_id,group_id_token):

        print("receive for a reservation")
        #Reserve a unspecified EVSE at a Charging Station
        if id!=0:  
            if connector_type!="Unknown":
                return call_result.ReserveNowPayload(
                    status="Accepted"
                )
            else:
                if evse_id==0:
                   return call_result.ReserveNowPayload(
                    status="Accepted"
            )
                else:
                    return  call_result.ReserveNowPayload(
                    status="Faulted"
            )
        else:
            return call_result.ReserveNowPayload(
                    status="Faulted"
            )

    @on('CancelReservation')
    def on_cancel_reservation(self , reservation_id):
        if reservation_id:
            print("cancel reservation is call from csms to cp")
            return call_result.CancelReservationPayload(status="Accepted")
        else:
            return call_result.CancelReservationPayload(status="Rejected")

#initiate rservation ended
    async def send_reservation_ended(self,reservation_id, reservation_update_status):
        print("reservation ended")
        request = call.ReservationStatusUpdatePayload(reservation_id=reservation_id,reservation_update_status=reservation_update_status)
        response = await self.call(request)
        print("----------------------------------------------",response)
        return response