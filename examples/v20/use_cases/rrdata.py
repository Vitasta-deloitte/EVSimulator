import sys
sys.path.append('../../../')
from examples.v20.use_cases.mainCp import conn, func

import asyncio
import websockets
import json

async def ss(action):
    while True:

        await asyncio.sleep(10)
        global acceptActionUnique,acceptRequestResponse, finalListRequest, finalListResponse
        acceptRequestResponse, acceptActionUnique=func()
        openRequest=acceptRequestResponse[acceptActionUnique[action]][0].index('{')
        closeRequest=acceptRequestResponse[acceptActionUnique[action]][0].rindex('}')
        openResponse=acceptRequestResponse[acceptActionUnique[action]][1].index('{')
        closeResponse=acceptRequestResponse[acceptActionUnique[action]][1].index('}')
        finalListRequest=json.loads(acceptRequestResponse[acceptActionUnique[action]][0][openRequest:closeRequest+1])
        finalListResponse=json.loads(acceptRequestResponse[acceptActionUnique[action]][1][openResponse:closeResponse+1])
        print("Request: ", finalListRequest)
        print("Response: ",finalListResponse)
        if 'status' in finalListResponse.keys():
            if finalListResponse['status']=='Accepted':
                await asyncio.create_task(ss("StatusNotification"))
            else:
                print("Status: ", "Rejected")


async def repeat_until_eternity():

    task1=asyncio.create_task(conn(var))
    # asyncio.create_task(ss("ReservationStatusUpdate"))
    # asyncio.create_task(ss("ReserveNow"))
    asyncio.create_task(ss("CancelReservation"))
    await asyncio.wait([task1])

def main(var1):
    global var
    var=var1
    asyncio.run(repeat_until_eternity())




