import sys
import asyncio
from examples.v20.use_cases.websocketSync import sync_client_server_websocket
def LogStatusNotificationValues(status,request_id):
    global var
    var=[f'charge_point_connection.send_diagnostic_log_status_notification("{status}",{request_id})']
    return asyncio.run(sync_client_server_websocket([],var))
def NotifyMonitoringReport(request_id,seq_no,generated_at):
    global var
    var =[f'charge_point_connection.send_diagnostic_notify_monitoring_report_request({request_id},{seq_no},"{generated_at}")']
    return asyncio.run(sync_client_server_websocket([],var))
def NotifyEvent(generated_at,tbc,seq_no,event_data):
    global var
    var= [f'charge_point_connection.send_diagnostic_notify_event_request("{generated_at}",{tbc},{seq_no},{event_data})']
    return asyncio.run(sync_client_server_websocket([],var))
def NotifyCustomerInformation(data,seq_no,generated_at,request_id):
    global var
    var = [f'charge_point_connection.send_diagnostic_notify_customer_information("{data}",{seq_no},"{generated_at}",{request_id})']
    return asyncio.run(sync_client_server_websocket([],var))

