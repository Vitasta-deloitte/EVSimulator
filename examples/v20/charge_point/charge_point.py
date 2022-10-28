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

# new1
async def nw(var):
    async with websockets.connect(
        'ws://localhost:9000/CP_1',
        subprotocols=['ocpp2.0']
    ) as ws:
        # global new1
        new1 = ChargePoint('CP_231', ws)
        print(new1)
        print("hit it", ws )
        # print(type(ws))
        
        # return new1
        # v=[]
        i=0
        while i<len(var):
            var[i]=eval(var[i])
            i+=1
        # print(var)
        # print(var)
        # print(var)
        # print(var)
        # await asyncio.gather(new1.send_transaction_event())
        # i=0
        # while i<len(var):
        # for i in range(len(var)-1,-1,-1):
            # print(var)
        await asyncio.gather(*var)
        # await asyncio.gather(var[2])
        # await asyncio.gather(var[0])
        #     # var[i]=eval(var[i])
        #     i+=1
        

# if __name__ == "__main__":
#     var1=['new1.start()','new1.send_transaction_event("Started","1666775586","CablePluggedIn",1,"1")','new1.send_boot_notification()']
#     asyncio.run(nw(var1))
    # asyncio.run() is used when running this example with Python >= 3.7v
#     asyncio.run(nw())
    # print(new1)
    # ChargePoint