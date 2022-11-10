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
# logging.basicConfig(level=
#         print(request)logging.INFO)

class ChargePoint(cp):

    @on("NotifyEVChargingNeeds")
    def on_notify_ev_charging_needs(self,charging_needs,evse_id,max_schedule_tuples):
        print('Notified EV Charging Needs')
        return call_result.NotifyEVChargingNeedsPayload(
            status="Accepted"
        )