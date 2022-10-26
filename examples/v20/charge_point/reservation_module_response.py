import asyncio
from doctest import master
import logging
from urllib import request
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

    @on('ReserveNow')
    def on_reservation(self , id , expiry_date_time, id_token,connector_type):
        print("receive for a reservation")
        return call_result.ReserveNowPayload(
            status="Accepted"
        )

    @on('CancelReservation')
    def on_cancel_reservation(self , reservation_id):
        print("cancel reservation is call from csms to cp")
        return call_result.CancelReservationPayload(status="Accepted")

#initiate rservation ended
    async def send_reservation_ended(self):
        print("reservation ended")
        request = call.ReservationStatusUpdatePayload(reservation_id=1,reservation_update_status="Expired")
        response = await self.call(request)