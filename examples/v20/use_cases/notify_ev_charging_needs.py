import sys
sys.path.append('../../../')
from examples.v20.use_cases.rrdata import main

def statusNotificationCases():
    global var
    var=[f'charge_point_connection.send_notify_ev_charging_needs_payload()']

statusNotificationCases()

main(var)