import asyncio
from mimetypes import init
from time import sleep
import websockets
from contextlib import suppress
import sys
sys.path.append('../../../')
from examples.v20.charge_point.charge_point import ChargePoint



async def repeat_until_eternity(charge_point_connection):
    while True:
        global returnRequestResponse, returnActionUnique
        returnRequestResponse=charge_point_connection.requestResponse
        returnActionUnique=charge_point_connection.actionUnique
        await asyncio.sleep(10)
        func()

async def conn(var):
    global returnRequestResponse,returnActionUnique
    returnRequestResponse,returnActionUnique={},{}
    
    async  with websockets.connect(
        'ws://localhost:9000/CP_1',
        subprotocols=['ocpp2.0']
    ) as ws:
        task=[]
        charge_point_connection = ChargePoint('CP_231', ws)
        task.append(asyncio.create_task(charge_point_connection.start()))
        for i in range(len(var)):
            task.append(asyncio.create_task(eval(var[i])))
        await asyncio.sleep(2)
        asyncio.create_task(repeat_until_eternity(charge_point_connection))
        await asyncio.wait([task[0]])

def func():
    return returnRequestResponse,returnActionUnique

if __name__ == "__main__":
    asyncio.run(conn([f'charge_point_connection.send_start_transaction()']))