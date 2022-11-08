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
from examples.v20.central_system.reservation_module_request import ChargePoint as cp
from examples.v20.central_system.onboot_response import ChargePoint as cp1
from examples.v20.central_system.charger_availability_request import ChargePoint as cp2
from examples.v20.central_system.transaction_module_request import ChargePoint as cp3
from examples.v20.central_system.diagnostics_module_response import ChargePoint as cp4
from examples.v20.central_system.status_notification_request import ChargePoint as cp5
from ocpp.v201 import call_result , call
from examples.v20.use_cases.csmsToCpForReservation import var as variable
from examples.v20.use_cases.csmsToCpForStatusNotification import var as variable1
from examples.v20.use_cases.csmsToCpForDiagnostic import variable as variable2

logging.basicConfig(level=logging.INFO)


class ChargePoint(cp,cp1,cp2,cp3,cp4,cp5):
    pass


async def on_connect(websocket, path):
    """ For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """
    try:
        requested_protocols = websocket.request_headers[
            'Sec-WebSocket-Protocol']
    except KeyError:
        logging.error(
            "Client hasn't requested any Subprotocol. Closing Connection"
        )
        return await websocket.close()
    if websocket.subprotocol:
        logging.info("Protocols Matched: %s", websocket.subprotocol)
    else:
        # In the websockets lib if no subprotocols are supported by the
        # client and the server, it proceeds without a subprotocol,
        # so we have to manually close the connection.
        logging.warning('Protocols Mismatched | Expected Subprotocols: %s,'
                        ' but client supports  %s | Closing connection',
                        websocket.available_subprotocols,
                        requested_protocols)
        return await websocket.close()

    charge_point_id = path.strip('/')
    cp = ChargePoint(charge_point_id, websocket)
    i=0
    actions=[]
    allActions=[]
    for i in range(len(variable1)):
        allActions.append(variable1[i])
    for i in range(len(variable)):
        allActions.append(variable[i])
    for i in range(len(variable2)):
        allActions.append(variable2[i])
    while i<len(allActions):
        actions.append(eval(allActions[i]))
        i+=1
    await asyncio.gather(cp.start(), *actions)


async def main():
    server = await websockets.serve(
        on_connect,
        '0.0.0.0',
        9000,
        subprotocols=['ocpp2.0']
    )

    logging.info("Server Started listening to new connections...")
    await server.wait_closed()


if __name__ == "__main__":
    # asyncio.run() is used when running this example with Python >= 3.7v
    asyncio.run(main())
