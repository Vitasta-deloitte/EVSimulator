import sys
sys.path.append('../../../')
from examples.v20.use_cases.websocketSync import sync_client_server_websocket
import asyncio

def reservationValues(reservation_id,reservation_update_status):
    global var
    var=[f'charge_point_connection.send_reservation_ended({reservation_id},"{reservation_update_status}")']
    return asyncio.run(sync_client_server_websocket([],var))