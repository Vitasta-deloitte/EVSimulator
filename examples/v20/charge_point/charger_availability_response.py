import asyncio
from doctest import master
import logging
from urllib import request
from datetime import datetime
import json as json
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

    async def send_charger_availability_notification_request(self):
        # Available ,Occupied ,Reserved, Unavailable, Faulted
        request = call.StatusNotificationPayload(timestamp= datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", connector_status= "Available", evse_id= 1, connector_id= 1)
        response = await self.call(request)
    
    @on('ChangeAvailability')
    def on_charger_availability(self, operational_status):
        print('Got a charger availability status')
        return call_result.ChangeAvailabilityPayload(
            status="Accepted"
        )
    
    async def send_charger_availability_notify_event_request(self):
        request = call.NotifyEventPayload(
            generated_at= datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z",
            seq_no= 0,
            event_data=[{
                'eventId':1, 
            "timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", 
            "trigger":"Alerting", 
            "actualValue":"2",
            "eventNotificationType":"CustomMonitor",
            "component":{
                "name":"Sneh"
                },
            "variable":{
                "name":"Sneh"
            }
            }]
        )
        response = await self.call(request)