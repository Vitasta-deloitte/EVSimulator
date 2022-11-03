
# Base of testing file
# DO NOT TOUCH

import asyncio
from mimetypes import init
from time import sleep
import websockets
from contextlib import suppress
import sys
sys.path.append('../../../')
from examples.v20.charge_point.charge_point import ChargePoint


async def conn():
    async  with websockets.connect(
        'ws://localhost:9000/CP_1',
        subprotocols=['ocpp2.0']
    ) as ws:
        charge_point_connection = ChargePoint('CP_231', ws)
        task2 = asyncio.create_task(charge_point_connection.start())
        task3 = asyncio.create_task(charge_point_connection.send_transaction_event("Started","1666775586","CablePluggedIn",1,"1",True))
        task4 = asyncio.create_task(charge_point_connection.send_boot_notification())
        await asyncio.sleep(2)
        # print(charge_point_connection.q1)
        asyncio.create_task(repeat_until_eternity(charge_point_connection))
        print(1)
        # await asyncio.wait([task5])
        await asyncio.wait([task2])


async def repeat_until_eternity(charge_point_connection):
    while True:
        print("-------------------------------")
        print(charge_point_connection.q1)
        await asyncio.sleep(10)

async def conn1():
    print("hit3")
    async  with websockets.connect(
        'ws://localhost:9000/CP_1',
        subprotocols=['ocpp2.0']
    ) as ws:
        charge_point_connection = ChargePoint('CP_231', ws)
        return await charge_point_connection.send_reservation_ended()

async def helper():
    task_1 = asyncio.create_task(conn())
    print(task_1)
    await asyncio.wait([task_1])

if __name__ == "__main__":
    asyncio.run(helper())