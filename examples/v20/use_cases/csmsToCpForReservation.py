import sys
import asyncio
sys.path.append('../../../')
from examples.v20.use_cases.websocketSync import sync_client_server_websocket

# Comparing date
# date="12/09/22"
# a = dt.strptime(expiry_date_time, "%d/%m/%y")
# b = dt.strptime(date, "%d/%m/%y")

# if b<=a:
#     expiry_date_time=expiry_date_time
# else:
#     id=0
def reservation(id, connector_type, evse_id,expiry_date_time, id_token, group_id_token):
    var=[]
    var.append(f'charge_point_connection.send_reservation({id},"{expiry_date_time}",{id_token},"{connector_type}",{evse_id},{group_id_token})')
    return asyncio.run(sync_client_server_websocket(var,[]))



def cancel_reservation(reservation_id):
    var=[]
    var.append(f'charge_point_connection.send_cancel_reservation({reservation_id})')
    return asyncio.run(sync_client_server_websocket(var,[]))