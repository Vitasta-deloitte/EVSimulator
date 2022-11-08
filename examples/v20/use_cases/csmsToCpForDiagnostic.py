variable =[]
def diagnosticGetLogRequest(log, log_type, request_id):
    var = f'cp.get_diagnostic_log_request({log},"{log_type}",{request_id})'
    variable.append(var)
def diagnosticGetMonitoringReport(request_id,monitoring_criteria, component_variables):
    var1 = f'cp.get_diagnostic_monitoring_report_request({request_id},{monitoring_criteria},{component_variables})'
    variable.append(var1)
def diagnosticSetMonitoringBase(monitoring_base):
    var2= f'cp.set_monitoring_base("{monitoring_base}")'
    variable.append(var2)
def diagnosticSetVariableMonitoring(monitoring_data):
    var3= f'cp.set_monitoring_variable({monitoring_data})'
    variable.append(var3)
def diagnosticSetMonitoringLevel(severity):
    var4= f'cp.set_monitoring_level({severity})'
    variable.append(var4)
def diagnosticClearMonitoringVariable(id):
    var5= f'cp.clear_variable_monitoring({id})'
    variable.append(var5)
def diagnosticCustomerInformation(request_id,report,clear):
    var6= f'cp.get_diagnostic_customer_information({request_id},{report},{clear})'
    variable.append(var6)


# diagnosticGetLogRequest({'remoteLocation':"remote.log"},"DiagnosticsLog",1)
# diagnosticGetMonitoringReport(1,["ThresholdMonitoring","DeltaMonitoring","PeriodicMonitoring"],[{"component":{"name":"Yukta"}}])
# diagnosticSetMonitoringBase("All")
# diagnosticSetVariableMonitoring([{'value':15,'type':"LowerThreshold",'severity':2,'component':{"name" :"helloThere"},'variable':{'name':"variable"}}])
# diagnosticClearMonitoringVariable([3])
# diagnosticSetMonitoringLevel(2)
# diagnosticCustomerInformation(1,True,False)