import sys
sys.path.append('../../../')
from examples.v20.use_cases.websocketSync import sync_client_server_websocket
import asyncio

def send_charger_availability_heartbeat(interval):
    var=[f'charge_point_connection.send_charger_availability_heartbeat({interval})']
    return asyncio.run(sync_client_server_websocket([],var))

import datetime

def send_charger_availability_notification_request(timestamp,connector_status,evse_id, connector_id):
    # timestamp=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
    var=[f'charge_point_connection.send_charger_availability_notification_request("{timestamp}","{connector_status}",{evse_id}, {connector_id})']
    return asyncio.run(sync_client_server_websocket([],var))


def send_charger_availability_notify_event_request(generated_at,seq_no, event_data):
    # event_data["timestamp"]=str(event_data["timestamp"])
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++",event_data)

    var=[f'charge_point_connection.send_charger_availability_notify_event_request("{generated_at}",{seq_no},{event_data})']
    return asyncio.run(sync_client_server_websocket([],var))


