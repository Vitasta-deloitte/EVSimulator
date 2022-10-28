import sys
sys.path.append('../../../')
# import examples.v20.charge_point.charge_point
from examples.v20.charge_point.charge_point import nw
from examples.v20.charge_point.charge_point import ChargePoint as cp99

import asyncio
import websockets

var=['new1.send_transaction_event("Started","1666775586","CablePluggedIn",1,"1")','new1.send_boot_notification()']
asyncio.run(nw(var))