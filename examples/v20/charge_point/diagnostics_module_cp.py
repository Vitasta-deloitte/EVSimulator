import logging
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
    async def send_diagnostic_log_status_notification(self,status,request_id):
        print("Send logging status notification")
        request = call.LogStatusNotificationPayload(
            status=status,
            request_id=request_id
            )
        response = await self.call(request)
        print(response)
    @on('GetMonitoringReport')
    def on_diagnostic_get_monitoring_report_request(self ,request_id,monitoring_criteria, component_variable):
        print("receive for get_monitoring_report_request")
        if monitoring_criteria == "ThresholdMonitoring" or monitoring_criteria =="DeltaMonitoring" or monitoring_criteria == "PeriodicMonitoring":
            return call_result.GetMonitoringReportPayload(
                status="Accepted"
            )
        if monitoring_criteria not in ["ThresholdMonitoring","DeltaMonitoring","PeriodicMonitoring"]:
            return call_result.GetMonitoringReportPayload(
                status="NotSupported"
            )
    @on('SetMonitoringBase')
    def on_set_monitoring_base(self,monitoring_base):
        print("monitoring base is set")
        if monitoring_base in ["All","FactoryDefault","HardWiredOnly"]:
            return call_result.SetMonitoringBasePayload(
                status = "Accepted"
            )
        if monitoring_base not in ["All","FactoryDefault","HardWiredOnly"]:
            return call_result.SetMonitoringBasePayload(
                status = "NotSupported"
            )
    @on('SetVariableMonitoring')
    def on_set_monitoring_variable(self,set_monitoring_data):
        print("monitoring base is set")
        if (set_monitoring_data[0]["type"]=="UpperThreshold" or set_monitoring_data[0]["type"]=="LowerThreshold") and (set_monitoring_data[0]["severity"]<0 or set_monitoring_data[0]["severity"]>9):
            return call_result.SetVariableMonitoringPayload(
                set_monitoring_result=[{
                    "status":"Rejected",
                    "type":set_monitoring_data[0]["type"],
                    "severity":set_monitoring_data[0]["severity"],
                    "component":set_monitoring_data[0]["component"],
                    "variable":set_monitoring_data[0]["variable"]
                }])
        elif set_monitoring_data[0]["type"] not in ["UpperThreshold","LowerThreshold","Delta","Periodic","PeriodicClockAligned"]:
            return call_result.SetVariableMonitoringPayload(
                set_monitoring_result=[{
                    "status":"UnsupportedMonitorType",
                    "type":set_monitoring_data[0]["type"],
                    "severity":set_monitoring_data[0]["severity"],
                    "component":set_monitoring_data[0]["component"],
                    "variable":set_monitoring_data[0]["variable"]
                }])
        else:
            return call_result.SetVariableMonitoringPayload(
                set_monitoring_result=[{
                    "status":"Accepted",
                    "type":set_monitoring_data[0]["type"],
                    "severity":set_monitoring_data[0]["severity"],
                    "component":set_monitoring_data[0]["component"],
                    "variable":set_monitoring_data[0]["variable"]
                }])
    @on('SetMonitoringLevel')
    def on_diagnostic_set_monitoring_level(self ,severity):
        print("monitor level is set")
        if severity<0 or severity>9:
            return call_result.SetMonitoringLevelPayload(
                status="Rejected"
            )
        else:
            return call_result.SetMonitoringLevelPayload(
                status="Accepted"
            )
    @on('ClearVariableMonitoring')
    def on_diagnostic_clear_variable_monitoring(self, id):
        print("cleared monitoring level")
        return call_result.ClearVariableMonitoringPayload(
            clear_monitoring_result=[{"status":"Accepted" , "id":id[0]}]
        )
    
    async def send_diagnostic_notify_monitoring_report_request(self,request_id,seq_no,generated_at):
        print("Send logging status notification")
        request = call.NotifyMonitoringReportPayload(
            request_id= request_id,
            seq_no= seq_no,
            generated_at= generated_at
            )
        response = await self.call(request)
        print(response)
    async def send_diagnostic_notify_event_request(self,generated_at,tbc,seq_no,event_data):
        print("Send notify event")
        request = call.NotifyEventPayload(
            generated_at= generated_at,
            tbc=tbc,
            seq_no= seq_no,
            event_data= event_data
            )
        response = await self.call(request)
    @on('CustomerInformation')
    def on_diagnostic_customer_iformation(self ,request_id, report, clear):
        print("receive for Customer Info")
        return call_result.CustomerInformationPayload(
            status="Accepted"
        )
    async def send_diagnostic_notify_customer_information(self,data,seq_no,generated_at,request_id):
        print("Send notification for customer info")
        request = call.NotifyCustomerInformationPayload(data= data,
        seq_no= seq_no,
        generated_at= generated_at,
        request_id= request_id)
        response = await self.call(request)