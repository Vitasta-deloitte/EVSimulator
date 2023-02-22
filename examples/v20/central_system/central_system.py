import asyncio
import logging
from datetime import datetime

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
from examples.v20.central_system.reservation_module_cs import ChargePoint as cp
from examples.v20.central_system.onboot_cs import ChargePoint as cp1
from examples.v20.central_system.charger_availability_cs import ChargePoint as cp2
from examples.v20.central_system.transaction_module_cs import ChargePoint as cp3
from examples.v20.central_system.diagnostics_module_cs import ChargePoint as cp4
from examples.v20.central_system.status_notification_cs import ChargePoint as cp5
from examples.v20.central_system.notify_ev_charging_needs_cs import ChargePoint as cp6

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp,cp1,cp2,cp3,cp4,cp5,cp6):
    pass
