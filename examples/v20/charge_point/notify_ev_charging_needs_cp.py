import logging
import sys 
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):
    
    async def send_notify_ev_charging_needs_payload(self, energyAmount, evEnergyCapacity):
        request = call.NotifyEVChargingNeedsPayload(
            charging_needs={"acChargingParameters":{"energyAmount":1, "evMinCurrent":2, "evMaxCurrent":3,"evMaxVoltage":4},"dcChargingParameters":{"evMaxCurrent":2,"evMaxVoltage":2,"energyAmount":energyAmount,"evMaxPower":2,"stateOfCharge":2,"evEnergyCapacity":evEnergyCapacity,"fullSoC":2,"bulkSoC":2},"requestedEnergyTransfer":"AC_single_phase","departureTime":"1666775586"},
            evse_id=2,
            max_schedule_tuples=2
            )
        response = await self.call(request)
        print("Call for Event Transaction")

    