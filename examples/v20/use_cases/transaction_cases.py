import sys
sys.path.append('../../../')
# import examples.v20.charge_point.charge_point
from examples.v20.use_cases.testing_cp import conn, func

import asyncio
import websockets
import json

event_type="Started"
timestamp="1666775586"
trigger_reason="CablePluggedIn"
seq_no=1
transactionId="1"
offline=True

var=[f'charge_point_connection.send_transaction_event("{event_type}","{timestamp}","{trigger_reason}",{seq_no},"{transactionId}",{offline})',f'charge_point_connection.send_start_transaction()']
# var=[f'charge_point_connection.send_start_transaction()']

async def ss(action):
    while True:

        await asyncio.sleep(10)
        acceptRequestResponse, acceptActionUnique=func()
        open=acceptRequestResponse[acceptActionUnique[action]][1].index('{')
        close=acceptRequestResponse[acceptActionUnique[action]][1].index('}')
        finalList=json.loads(acceptRequestResponse[acceptActionUnique[action]][1][open:close+1])
        print(finalList)


async def repeat_until_eternity(var):
    task1=asyncio.create_task(conn(var))
    asyncio.create_task(ss("RequestStartTransaction"))
    asyncio.create_task(ss("TransactionEvent"))
    await asyncio.wait([task1])

asyncio.run(repeat_until_eternity(var))


