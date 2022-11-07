import sys
sys.path.append('../../../')
from examples.v20.use_cases.rrdata import main

def reservationValues(reservation_id,reservation_update_status):
    global var
    # var=[f'charge_point_connection.send_reservation_ended({reservation_id},"{reservation_update_status}")']
    var=""

reservationValues(1,"Expired")

main(var)