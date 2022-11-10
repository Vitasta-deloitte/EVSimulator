import sys
sys.path.append('../../../')
from examples.v20.use_cases.mainCp import conn, func

import asyncio
import json

async def ss(action):
    global energy_required
    energy_required=0
    while True:
        await asyncio.sleep(10)
        global acceptActionUnique,acceptRequestResponse, finalListRequest, finalListResponse
        acceptRequestResponse, acceptActionUnique=func()
        openRequest=acceptRequestResponse[acceptActionUnique[action]][0].index('{')
        closeRequest=acceptRequestResponse[acceptActionUnique[action]][0].rindex('}')
        openResponse=acceptRequestResponse[acceptActionUnique[action]][1].index('{')
        closeResponse=acceptRequestResponse[acceptActionUnique[action]][1].rindex('}')
        finalListRequest=json.loads(acceptRequestResponse[acceptActionUnique[action]][0][openRequest:closeRequest+1])
        finalListResponse=json.loads(acceptRequestResponse[acceptActionUnique[action]][1][openResponse:closeResponse+1])
        print("Request: ", finalListRequest)
        print("Response: ",finalListResponse)
        if action=="ReserveNow":
            if 'connectorType' in finalListRequest.keys() and 'status' in finalListResponse.keys():
                if finalListRequest['connectorType'] not in ["Unknown", "Undetermined"] and finalListResponse['status']=='Accepted':
                    await asyncio.create_task(ss("StatusNotification"))
                else:
                    print("Status: ", "Rejected")

        if action=="CancelReservation":
            if 'status' in finalListResponse.keys() and finalListResponse['status']=='Accepted':
                await asyncio.create_task(ss("StatusNotification"))
            else:
                    print("Status: ", "Rejected")

        if action=="NotifyEVChargingNeeds":
            if energy_required:
                energy_required=energy_required-1000
            else:
                energy_required=finalListRequest["chargingNeeds"]["dcChargingParameters"]["energyAmount"]
            max_energy=finalListRequest["chargingNeeds"]["dcChargingParameters"]["evEnergyCapacity"]
            energy_remaining=max_energy-energy_required
            max_charging_done=(max_energy*80/100)
            if energy_remaining<=max_charging_done:
                max_energy_provided=max_charging_done-energy_remaining
                print("Energy that can be provided to the user for getting the value to 80%: ", max_energy_provided)
            else:
                print("Vehicle already charged upto 80% or above and hence charging is stopped")
                break

        if action=="TransactionEvent":
            if "updatedPersonalMessage" in finalListResponse:
                if "content" in finalListResponse["updatedPersonalMessage"] and finalListResponse["updatedPersonalMessage"]["content"]=="Disconnected":
                    break
            

async def repeat_until_eternity():

    task1=asyncio.create_task(conn(var))

    # asyncio.create_task(ss("ReservationStatusUpdate"))
    asyncio.create_task(ss("ReserveNow"))
    # asyncio.create_task(ss("CancelReservation"))

    # asyncio.create_task(ss("GetLog"))
    # asyncio.create_task(ss("LogStatusNotification"))
    # asyncio.create_task(ss("GetMonitoringReport"))
    # asyncio.create_task(ss("SetMonitoringBase"))
    # asyncio.create_task(ss("SetVariableMonitoring"))
    # asyncio.create_task(ss("NotifyMonitoringReport"))
    # asyncio.create_task(ss("SetMonitoringLevel"))
    # asyncio.create_task(ss("ClearVariableMonitoring"))
    # asyncio.create_task(ss("NotifyEvent"))
    # asyncio.create_task(ss("CustomerInformation"))
    # asyncio.create_task(ss("NotifyCustomerInformation"))


    # asyncio.create_task(ss("TransactionEvent"))
    # asyncio.create_task(ss("NotifyEVChargingNeeds"))
    await asyncio.wait([task1])



def main(var1):
    global var
    var=var1
        
    asyncio.run(repeat_until_eternity())




