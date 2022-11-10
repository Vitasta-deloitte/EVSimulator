import logging
import sys 
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result
logging.basicConfig(level=logging.INFO)
class ChargePoint(cp):

    @on('StatusNotification')
    def on_status_notification(self,timestamp,connector_status,evse_id,connector_id):
        return call_result.StatusNotificationPayload(
        )