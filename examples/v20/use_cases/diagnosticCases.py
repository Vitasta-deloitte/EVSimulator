import sys
sys.path.append('../../../')
from examples.v20.use_cases.rrdata import main
from datetime import datetime
def LogStatusNotificationValues(status,request_id):
    global v1
    v1=[f'charge_point_connection.send_diagnostic_log_status_notification("{status}",{request_id})']
    
def NotifyMonitoringReport(request_id,seq_no,generated_at):
    global v2
    v2 =[f'charge_point_connection.send_diagnostic_notify_monitoring_report_request({request_id},{seq_no},"{generated_at}")']
def NotifyEvent(generated_at,tbc,seq_no,event_data):
    global v3
    v3= [f'charge_point_connection.send_diagnostic_notify_event_request("{generated_at}",{tbc},{seq_no},{event_data})']
def NotifyCustomerInformation(data,seq_no,generated_at,request_id):
    global v4
    v4 = [f'charge_point_connection.send_diagnostic_notify_customer_information("{data}",{seq_no},"{generated_at}",{request_id})']
LogStatusNotificationValues("Uploading",123)
NotifyMonitoringReport(2,3,"12/10/22")
NotifyEvent("12/10/22",False,2,[{'eventId':1,"timestamp":"12/10/22","trigger":"Alerting","actualValue":"2","eventNotificationType":"CustomMonitor","component":{"name":"Sneh"},"variable":{"name":"Sneh"}}])
NotifyCustomerInformation("yessss",2,"12/23/2022",9)
# main(v1)
# main(v2)
# main(v3)
# main(v4)