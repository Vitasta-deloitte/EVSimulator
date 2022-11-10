import logging
from datetime import datetime
import sys
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.charge_point import ChargePoint as cp
from ocpp.v201 import call_result , call;

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp):
    @on('BootNotification')
    def on_boot_notification(self, charging_station, reason, **kwargs):
        print("call from client")
        return call_result.BootNotificationPayload(
            current_time=datetime.utcnow().isoformat(),
            interval=10,
            status='Accepted'
        )
