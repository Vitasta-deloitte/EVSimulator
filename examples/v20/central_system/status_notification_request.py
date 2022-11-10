import logging
import sys
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call_result , call;
logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):

    async def send_status_notification(self,timestamp,connector_status,evse_id,connector_id):
        request = call.StatusNotificationPayload(
            timestamp= timestamp, 
            connector_status= connector_status,
            evse_id= evse_id, 
            connector_id= connector_id)
        response = await self.call(request)
        print("calll for a status notification")
        print(response)