import logging
import sys
sys.path.append('../../../')
from ocpp.routing import on
from ocpp.v201 import ChargePoint as cp
from ocpp.v201 import call_result , call;
logging.basicConfig(level=logging.INFO)
class ChargePoint(cp):

    async def get_diagnostic_log_request(self,log, log_type, request_id):
        request = call.GetLogPayload(
        log= log,
        log_type= log_type,
        request_id= request_id
        )
        response = await self.call(request)
        print("Call for 1st function")
        print(response)

    @on('LogStatusNotification')
    def on_diagnostic_log_status_notification(self,status,request_id):
        print("Receive for a Log Status Notification Transaction")
        if status=="Uploading":
            return call_result.LogStatusNotificationPayload()
        if status=="Uploaded":
            return call_result.LogStatusNotificationPayload()

    async def get_diagnostic_monitoring_report_request(self,request_id,monitoring_criteria, component_variable):
        request = call.GetMonitoringReportPayload(
        request_id= request_id,
        monitoring_criteria = monitoring_criteria,
        component_variable = component_variable
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
    def on_diagnostic_notify_event(self, generated_at,tbc ,seq_no ,event_data):
        print("Receive for Notify Event")
        return call_result.NotifyEventPayload(
        )
        
    async def get_diagnostic_customer_information(self,request_id,report,clear):
        request = call.CustomerInformationPayload(
        request_id= request_id,
        report= report,
        clear= clear
        )
        response = await self.call(request)
        print("Call for Customer Info")
        print(response)

    async def set_monitoring_base(self,monitoring_base):
        print("set monitoring base")
        request = call.SetMonitoringBasePayload(monitoring_base=monitoring_base)
        response = await self.call(request)
        print(response)

    async def set_monitoring_variable(self,monitoring_data):
        print("set monitoring variable")
        request = call.SetVariableMonitoringPayload(set_monitoring_data=monitoring_data)
        response = await self.call(request)
        print(response)

    async def clear_variable_monitoring(self,id):
        print("clear monitoring variable")
        request = call.ClearVariableMonitoringPayload(id=id)
        response = await self.call(request)
        print(response)

    async def set_monitoring_level(self,severity):
        print("set monitoring level")
        request = call.SetMonitoringLevelPayload(severity=severity)
        response = await self.call(request)
        print(response)
        
    @on('NotifyCustomerInformation')
    def on_diagnostic_notify_customer(self, data,seq_no,generated_at,request_id):
        print("Receive for notify Customer Info")
        return call_result.NotifyCustomerInformationPayload(
        )