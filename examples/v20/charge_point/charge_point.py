import asyncio
from doctest import master
import logging

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
from examples.v20.charge_point.charger_availability_response import ChargePoint as cp
from examples.v20.charge_point.onboot_request import ChargePoint as cp1
from examples.v20.charge_point.reservation_module_response import ChargePoint as cp2
from examples.v20.charge_point.transaction_module_response import ChargePoint as cp3
from examples.v20.charge_point.diagnostics_module_request import ChargePoint as cp4

from ocpp.v201 import call, call_result

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp,cp1,cp2,cp3,cp4):
    pass

async def main():
    async with websockets.connect(
        'ws://localhost:9000/CP_1',
        subprotocols=['ocpp2.0']
    ) as ws:

        cp = ChargePoint('CP_231', ws)
        print("hit it", ws )
        print(type(ws))
        await asyncio.gather(cp.start())


if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
