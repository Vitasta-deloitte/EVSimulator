import asyncio
import logging
from datetime import datetime

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
from ocpp.v201 import call_result , call;

logging.basicConfig(level=logging.INFO)

class ChargePoint(cp):

    async def get_diagnostic_log_request(self):
        request = call.GetLogPayload(
            log= {'remoteLocation':'Ranchi'},
            log_type= "DiagnosticsLog",
            request_id= 1
            )
        response = await self.call(request)
        print("Call for 1st function")
        print(response)

    @on('LogStatusNotification')
    def on_diagnostic_log_status_notification(self, status):
        print("Receive for a Log Status Notification Transaction")
        return call_result.LogStatusNotificationPayload(
        )
   
    async def get_diagnostic_monitoring_report_request(self):
        request = call.GetMonitoringReportPayload(
            request_id= 2
            )
        response = await self.call(request)
        print("Call for MonitoringReportPayload")
        print(response)

    @on('NotifyMonitoringReport')
    def on_diagnostic_notify_monitoring_report(self, request_id,seq_no,generated_at):
        print("Receive for a Log Status Notification Transaction")
        return call_result.NotifyMonitoringReportPayload(
        )
    
    @on('NotifyEvent')
    def on_diagnostic_notify_event(self, generated_at ,seq_no ,event_data):
        print("Receive for Notify Event")
        return call_result.NotifyEventPayload(
        )

    async def get_diagnostic_customer_information(self):
        request = call.CustomerInformationPayload(
            request_id= 1,
            report= True,
            clear= True
            )
        response = await self.call(request)
        print("Call for Customer Info")
        print(response)

    @on('NotifyCustomerInformation')
    def on_diagnostic_notify_event(self, data,seq_no,generated_at,request_id):
        print("Receive for Customer Info")
        return call_result.NotifyCustomerInformationPayload(
        )
    
