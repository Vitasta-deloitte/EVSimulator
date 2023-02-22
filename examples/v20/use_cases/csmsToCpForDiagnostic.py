import sys
import asyncio
sys.path.append('../../../')
from examples.v20.use_cases.websocketSync import sync_client_server_websocket
def diagnosticGetLogRequest(log, log_type, request_id):
    variable =[]
    variable.append( f'charge_point_connection.get_diagnostic_log_request({log},"{log_type}",{request_id})')
    return asyncio.run(sync_client_server_websocket(variable,[]))
def diagnosticGetMonitoringReport(request_id,monitoring_criteria, component_variables):
    variable =[]
    var = f'charge_point_connection.get_diagnostic_monitoring_report_request({request_id},{monitoring_criteria},{component_variables})'
    variable.append(var)
    return asyncio.run(sync_client_server_websocket(variable,[]))
def diagnosticSetMonitoringBase(monitoring_base):
    variable =[]
    var= f'charge_point_connection.set_monitoring_base("{monitoring_base}")'
    variable.append(var)
    return asyncio.run(sync_client_server_websocket(variable,[]))
def diagnosticSetVariableMonitoring(monitoring_data):
    variable =[]
    var= f'charge_point_connection.set_monitoring_variable({monitoring_data})'
    variable.append(var)
    return asyncio.run(sync_client_server_websocket(variable,[]))

def diagnosticSetMonitoringLevel(severity):
    variable =[]
    var= f'charge_point_connection.set_monitoring_level({severity})'
    variable.append(var)
    return asyncio.run(sync_client_server_websocket(variable,[]))

def diagnosticClearMonitoringVariable(id):
    variable =[]
    var= f'charge_point_connection.clear_variable_monitoring({id})'
    variable.append(var)
    return asyncio.run(sync_client_server_websocket(variable,[]))

def diagnosticCustomerInformation(request_id,report,clear):
    variable =[]
    var= f'charge_point_connection.get_diagnostic_customer_information({request_id},{report},{clear})'
    variable.append(var)
    return asyncio.run(sync_client_server_websocket(variable,[]))

