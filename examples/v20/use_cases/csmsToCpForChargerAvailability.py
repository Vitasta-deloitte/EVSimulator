import sys
import asyncio
sys.path.append('../../../')
from examples.v20.use_cases.websocketSync import sync_client_server_websocket

def get_charger_availability_change_availability(operational_status,evse):
    var=[]
    var.append(f'charge_point_connection.get_charger_availability_change_availability("{operational_status}",{evse})')
    return asyncio.run(sync_client_server_websocket(var,[]))
