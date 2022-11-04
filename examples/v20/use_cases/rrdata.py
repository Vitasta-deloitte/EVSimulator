import sys
sys.path.append('../../../')
# import examples.v20.charge_point.charge_point
from examples.v20.use_cases.mainCp import conn, func
# from examples.v20.use_cases.user import var

import asyncio
import websockets
import json

async def ss(action):
    while True:

        await asyncio.sleep(10)
        acceptRequestResponse, acceptActionUnique=func()
        openRequest=acceptRequestResponse[acceptActionUnique[action]][0].index('{')
        closeRequest=acceptRequestResponse[acceptActionUnique[action]][0].rindex('}')
        openResponse=acceptRequestResponse[acceptActionUnique[action]][1].index('{')
        closeResponse=acceptRequestResponse[acceptActionUnique[action]][1].index('}')
        finalListRequest=json.loads(acceptRequestResponse[acceptActionUnique[action]][0][openRequest:closeRequest+1])
        finalListResponse=json.loads(acceptRequestResponse[acceptActionUnique[action]][1][openResponse:closeResponse+1])
        print("Request: ", finalListRequest)
        print("Response: ",finalListResponse)


async def repeat_until_eternity():

    #Data value is passed as var which is imported from user.py via main function
    task1=asyncio.create_task(conn(var))

    #All the tasks are created here whether it is CSMS to CP or CP to CSMS
    asyncio.create_task(ss("ReserveNow"))
    # asyncio.create_task(ss("RequestStartTransaction"))
    asyncio.create_task(ss("TransactionEvent"))
    await asyncio.wait([task1])

def main(var1):
    global var
    var=var1
    asyncio.run(repeat_until_eternity())




