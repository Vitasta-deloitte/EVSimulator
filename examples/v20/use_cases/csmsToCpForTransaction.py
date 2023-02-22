
import sys
import asyncio
sys.path.append('../../../')
from examples.v20.use_cases.websocketSync import sync_client_server_websocket

def get_transaction_status(transaction_id):
    var=[]
    var.append(f'charge_point_connection.get_transaction_transaction_status("{transaction_id}")')
    return asyncio.run(sync_client_server_websocket(var,[]))