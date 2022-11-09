import sys
sys.path.append('../../../')
from examples.v20.use_cases.rrdata import main

def transactionValues(event_type,timestamp,trigger_reason,seq_no,transactionId,number_of_phases_used,cable_max_current,reservation_id,evse,id_token,offline):
    global var
    var=[f'charge_point_connection.send_transaction_event("{event_type}","{timestamp}","{trigger_reason}",{seq_no},"{transactionId}",{number_of_phases_used},{cable_max_current},{reservation_id},{evse},{id_token},{offline})']


transactionValues("Started", "1666775586","EVDetected",1,"1",2,2,2,{"id":2},{"idToken":"22","type":"Central"},True)

main(var)