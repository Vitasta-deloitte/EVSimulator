import asyncio
import websockets
import logging
import sys
import time
sys.path.append('../../../')
from examples.v20.central_system.central_system import ChargePoint

logging.basicConfig(level=logging.INFO)

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
    charge_point_connection = ChargePoint(charge_point_id, websocket)

    task=[]
    task.append(asyncio.create_task(charge_point_connection.start()))
    for i in range(len(var)):
        task.append(asyncio.create_task(eval(var[i])))
    await asyncio.wait([task[0]])

    await websocket.wait_closed()

    


async def main(vars,port):
    global var
    var = vars

    server =  await websockets.serve(
            on_connect,
            '0.0.0.0',
            port,
            subprotocols=['ocpp2.0']
        )
 
    logging.info("Server Started listening to new connections...")



    

