import asyncio
import logging
from datetime import datetime
import json as json
import sys 
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result
import re
logging.basicConfig(level=logging.INFO)

def date_hook(json_dict):
        for (key, value) in json_dict.items():
            try:
                json_dict[key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
            except:
                pass
        return json_dict
class ChargePoint(cp):

    async def send_charger_availability_heartbeat(self, interval):
        request = call.HeartbeatPayload()
        while True:
            await self.call(request)
            await asyncio.sleep(interval)

    async def send_charger_availability_notification_request(self,timestamp,connector_status,evse_id, connector_id):
        # Available ,Occupied ,Reserved, Unavailable, Faulted
        request = call.StatusNotificationPayload(
            timestamp= timestamp, 
            connector_status= connector_status, 
            evse_id= evse_id, 
            connector_id= connector_id)
        response = await self.call(request)
    
    @on('ChangeAvailability')
    def on_charger_availability(self, operational_status):
        print('Got a charger availability status')
        return call_result.ChangeAvailabilityPayload(
            status="Accepted"
        )
    
    async def send_charger_availability_notify_event_request(self,generated_at,seq_no,event_data):
        request = call.NotifyEventPayload(
            generated_at= generated_at,
            seq_no= seq_no,
            event_data=event_data
        )
        response = await self.call(request)