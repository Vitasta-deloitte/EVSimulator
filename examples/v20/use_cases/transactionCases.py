import sys
sys.path.append('../../../')
from examples.v20.use_cases.rrdata import main

event_type="Started"
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

def transactionValues():
    global var
    var=[]
    var.append(f'charge_point_connection.send_transaction_event("{event_type}","{timestamp}","{trigger_reason}",{seq_no},{transaction_info},{number_of_phases_used},{cable_max_current},{reservation_id},{evse},{id_token},{offline},{meter_value})')


# S1: EV connected
event_type="Started"
transaction_info["charging_state"]="EVConnected"

# S2: Battery Percentage


transactionValues()
main(var)