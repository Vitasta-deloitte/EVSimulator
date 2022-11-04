import sys
sys.path.append('../../../')
from examples.v20.use_cases.rrdata import main

def transactionValues(event_type,timestamp,trigger_reason,seq_no,transactionId,offline):
    global var
    var=[f'charge_point_connection.send_transaction_event("{event_type}","{timestamp}","{trigger_reason}",{seq_no},"{transactionId}",{offline})']

transactionValues("Started", "1666775586","EVDetected",1,"1",True)

main(var)