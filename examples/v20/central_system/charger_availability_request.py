import asyncio
import logging
from datetime import datetime
from urllib import response
now = datetime.now()
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
from ocpp.charge_point import ChargePoint as cp
from ocpp.v201 import call_result , call;
logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):

    @on('Heartbeat')
    def on_heartbeat(self):
        print('Got a Heartbeat!')
        return call_result.HeartbeatPayload(
            current_time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
        )

    @on('StatusNotification')
    def on_status_notification(self,timestamp, connector_status, evse_id, connector_id):
        print("return a  status request")
        return call_result.StatusNotificationPayload()

    async def get_charger_availability(self):
        request = call.ChangeAvailabilityPayload(
            operational_status="Inoperative")
        response = await self.call(request)
        print("Call for status of charger availability")
        print(response)
    
    @on('NotifyEvent')
    def on_notify_event_request(self,generated_at, seq_no, event_data):
        print("return notify event request")
        return call_result.NotifyEventPayload()