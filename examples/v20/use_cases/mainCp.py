import asyncio
from mimetypes import init
from time import sleep
import websockets
from contextlib import suppress
import sys
sys.path.append('../../../')
from examples.v20.charge_point.charge_point import ChargePoint

async def repeat_until_eternity(charge_point_connection):
        global returnRequestResponse, returnActionUnique
        returnRequestResponse=charge_point_connection.requestResponse
        returnActionUnique=charge_point_connection.actionUnique
        await asyncio.sleep(10)
        func()

async def conn(var,port):
    global returnRequestResponse,returnActionUnique
    returnRequestResponse,returnActionUnique={},{}
    
    async  with websockets.connect(
        f'ws://localhost:{port}/CP_1',
        subprotocols=['ocpp2.0']
    ) as ws:
        task=[]
        charge_point_connection = ChargePoint('CP_1', ws)
        charge_point_connection.actionUnique = {}
        charge_point_connection.requestResponse = {}
        task.append(asyncio.create_task(charge_point_connection.start()))
        for i in range(len(var)):
            task.append(asyncio.create_task(eval(var[i])))
        await asyncio.sleep(2)
        asyncio.create_task(repeat_until_eternity(charge_point_connection))
        await asyncio.wait([task[0]])
        await ws.close()

def func():
    return returnRequestResponse,returnActionUnique
