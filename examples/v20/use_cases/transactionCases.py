import sys
sys.path.append('../../../')
from examples.v20.use_cases.rrdata import main

def transactionValues():
    global var
    var=[f'charge_point_connection.send_transaction_event("{event_type}","{timestamp}","{trigger_reason}",{seq_no},"{transactionId}",{number_of_phases_used},{cable_max_current},{reservation_id},{evse},{id_token},{offline},{meter_value})']
    
event_type="Started"
timestamp="1666775586"
trigger_reason="EVDetected"
seq_no=1
transactionId="1"
number_of_phases_used=2
cable_max_current=2
reservation_id=2
evse={"id":2}
id_token={"idToken":"22","type":"Central"}
offline=True
meter_value=[{"timestamp":"1666775586","sampledValue":[{"value":2}]}]

transactionValues()

main(var)