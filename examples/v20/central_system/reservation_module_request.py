import asyncio
import logging
from datetime import datetime
from urllib import response
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

    #send reservation using reservenowrequest and resrvenowresponse
    async def send_reservation(self,id,expiry_date_time,id_token,connector_type,evse_id,group_id_token):
        request = call.ReserveNowPayload(
            id= id, 
            expiry_date_time= expiry_date_time,
            id_token=id_token,
            connector_type= connector_type, 
            evse_id= evse_id, 
            group_id_token= group_id_token)
        response = await self.call(request)
        print("calll for a reservation")
        print(response)
        if response.status == 'Accepted':
            print("reservation is  booked")

    #cancel reservation csms to cp 
    async def send_cancel_reservation(self, reservation_id):
        request = call.CancelReservationPayload(
            reservation_id = reservation_id
            )
        response = await self.call(request)
        print("call for cancel reservation")
        if response.status == 'Accepted':
            print("cancel reservation is  completed")

    @on('ReservationStatusUpdate')
    def on_reservation_ended(self ,reservation_id,reservation_update_status):
        if(reservation_update_status=="Expired"):
            return call_result.ReservationStatusUpdatePayload(    
            )