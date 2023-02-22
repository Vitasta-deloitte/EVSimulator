import sys
import asyncio
from examples.v20.use_cases.websocketSync import sync_client_server_websocket


# event_type="Started"
timestamp="1666775586"
trigger_reason="CablePluggedIn"
seq_no=1
transaction_info={"transaction_id":"2","charging_state":"EVConnected"}
number_of_phases_used=2
cable_max_current=2
reservation_id=2
evse={"id":2}
id_token={"idToken":"22","type":"Central"}
offline=True
meter_value=[{"timestamp":"1666775586","sampledValue":[{"value":2}]}]

def transactionValues(event_type,timestamp,trigger_reason,seq_no,transaction_info,number_of_phases_used,cable_max_current,reservation_id,evse,id_token,offline,meter_value):
    global var
    var=[]
    var=[f'charge_point_connection.send_transaction_event("{event_type}","{timestamp}","{trigger_reason}",{seq_no},{transaction_info},{number_of_phases_used},{cable_max_current},{reservation_id},{evse},{id_token},{offline},{meter_value})']
    return asyncio.run(sync_client_server_websocket([],var))

# S1: EV connected
# event_type="Started"
# transaction_info["charging_state"]="EVConnected"
# transactionValues()

# S2 and S3: For battery percentage and continuous evaluation of battery
def statusNotificationCases(energyAmount,evEnergyCapacity):
    global var
    var=[f'charge_point_connection.send_notify_ev_charging_needs_payload({energyAmount},{evEnergyCapacity})']
    return asyncio.run(sync_client_server_websocket([],var))


# energyAmount=3500
# evEnergyCapacity=5000
# statusNotificationCases()

# S4: User Disconnected the EV 
# transaction_info={"transaction_id":"2","charging_state":"EVConnected","stoppedReason":"EVDisconnected"}
# transactionValues()   


