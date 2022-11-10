import sys
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.charge_point import ChargePoint as cp
from ocpp.v201 import call_result , call

class ChargePoint(cp):

    @on("NotifyEVChargingNeeds")
    def on_notify_ev_charging_needs(self,charging_needs,evse_id,max_schedule_tuples):
        print('Notified EV Charging Needs')
        return call_result.NotifyEVChargingNeedsPayload(
            status="Accepted"
        )