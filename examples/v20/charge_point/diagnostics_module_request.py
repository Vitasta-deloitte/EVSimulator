import asyncio
from datetime import datetime
from doctest import master
import logging
from urllib import request
try:
    import websockets
except ModuleNotFoundError:
    print("This example relies on the 'websockets' package.")
    print("Please install it by running: ")
    print()
    print(" $ pip install websockets")
    import sys
    sys.exit(1)
import sys 
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call, call_result
logging.basicConfig(level=logging.INFO)
class ChargePoint(cp):

    @on('GetLog')
    def on_diagnostic_logging(self ,log, log_type, request_id):
        print("receive for 1st log request")
        return call_result.GetLogPayload(
            status="Accepted"
        )
    
    async def send_diagnostic_log_status_notification(self):
        print("Send logging status notification")
        request = call.LogStatusNotificationPayload(status="Accepted")
        response = await self.call(request)

    @on('GetMonitoringReport')
    def on_diagnostic_get_monitoring_report_request(self ,request_id):
        print("receive for get_monitoring_report_request")
        return call_result.GetMonitoringReportPayload(
            status="Accepted"
        )
    
    async def send_diagnostic_notify_monitoring_report_request(self):
        print("Send logging status notification")
        request = call.NotifyMonitoringReportPayload(
            request_id= 2,
            seq_no= 3,
            generated_at= datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z"
            )
        response = await self.call(request)
    
    async def send_diagnostic_notify_event_request(self):
        print("Send notify event")
        request = call.NotifyEventPayload(
            generated_at= datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z",
            seq_no= 2,
            event_data= [{
                'eventId':1, 
            "timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", 
            "trigger":"Alerting", 
            "actualValue":"2",
            "eventNotificationType":"CustomMonitor",
            "component":{
                "name":"Sneh"
                },
            "variable":{
                "name":"Sneh"
            }
            }])
        response = await self.call(request)
    
    @on('CustomerInformation')
    def on_diagnostic_customer_imformation(self ,request_id, report, clear):
        print("receive for Customer Info")
        return call_result.CustomerInformationPayload(
            status="Accepted"
        )

    async def send_diagnostic_notify_customer_information(self):
        print("Send notification for customer info")
        request = call.NotifyCustomerInformationPayload(data= "Subscribe To MiniMeYT",
        seq_no= 4,
        generated_at= datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z",
        request_id= 0)
        response = await self.call(request)