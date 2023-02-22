from flask import Flask
from flask import request

app = Flask(__name__)
import sys
import json
sys.path.append("../../../")
import asyncio
from examples.v20.charge_point.charge_point import ChargePoint as cp
import examples.v20.use_cases.transactionCases as transactioncp
import examples.v20.use_cases.csmsToCpForReservation as reservation
import examples.v20.use_cases.csmsToCpForTransaction as transaction
import examples.v20.use_cases.csmsToCpForDiagnostic as diagnostic
import examples.v20.use_cases.csmsToCpForChargerAvailability as availability
import examples.v20.use_cases.reservationCases as reservationcp
import examples.v20.use_cases.chargerAvailabilityCases as availabilitycp
import examples.v20.use_cases.diagnosticCases as diagnosticcp

from examples.v20.flask.jsonData import json_response 


@app.route("/chargeremaining",  methods=["POST"])
def status_notification():
    data=request.get_json()
    res ,req = transactioncp.statusNotificationCases(data["energyAmount"],data["evEnergyCapacity"])
    return json_response("NotifyEVChargingNeeds",res ,req)

import logging
@app.route("/reserve/booking", methods=["POST"])
def send_reservation():
    try:
        data=request.get_json()
        
        res ,req = reservation.reservation(data["id"],data["connector_type"],data["evse_id"],data["expiry_date_time"], data["id_token"], data["group_id_token"])
        s=json_response("ReserveNow",res ,req)
        s=json.loads(s)
        d={}
        d["ReserveNow"]=s
        l=status_notification()
        d["StatusNotification"]=json.loads(l)
        if s["Request"]["connectorType"] in ["Unknown", "Undetermined"] or s["Response"]["status"]!='Accepted':
            d["StatusNotification"]["Response"]["status"]="Rejected"
        return d
    except Exception as e:
        e=str(e)
        return e
    
@app.route("/reserve/cancel", methods=["POST"])
def send_cancel_reservation():
    try:
        data=request.get_json()
        res,req = reservation.cancel_reservation(data["reservation_id"])
        d={}
        s=json_response("CancelReservation", res, req)
        s=json.loads(s)
        d["CancelReservation"]=s
        l=status_notification()
        d["StatusNotification"]=json.loads(l)
        if s["Response"]["status"]!='Accepted':
            d["StatusNotification"]["Response"]["status"]="Rejected"
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/reserve/ended", methods=["POST"])
def send_reservation_ended():
    try:
        data=request.get_json()
        res, req = reservationcp.reservationValues(data["reservation_id"],data["reservation_update_status"])
        d={}
        s=json_response("ReservationStatusUpdate", res, req)
        s=json.loads(s)
        d["ReservationEnded"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/transaction/status", methods=["POST"])
def send_transaction_status():
    try:
        data=request.get_json()
        res,req = transaction.get_transaction_status(data["transaction_id"])
        d={}
        s=json_response("GetTransactionStatus", res, req)
        s=json.loads(s)
        d["TransactionStatus"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/transaction/values", methods=["POST"])
def send_transaction_values():
    try:
        data=request.get_json()
        res, req = transactioncp.transactionValues(data["event_type"],data["timestamp"],data["trigger_reason"],data["seq_no"],data["transaction_info"],data["number_of_phases_used"],data["cable_max_current"],data["reservation_id"],data["evse"],data["id_token"],data["offline"],data["meter_value"])
        d={}
        s=json_response("TransactionEvent", res, req)
        s=json.loads(s)
        d["TransactionValues"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

def log_status_notification():
    data=request.get_json()
    res ,req = diagnosticcp.LogStatusNotificationValues(data["status"],data["request_id"])
    return json_response("LogStatusNotification",res ,req)

@app.route("/diagnostic/getLog", methods=["POST"])
def get_log_request():
    try:
        data=request.get_json()
        res,req = diagnostic.diagnosticGetLogRequest(data["log"],data["log_type"],data["request_id"])
        d={}
        s=json_response("GetLog", res, req)
        s=json.loads(s)
        d["GetLog"]=s
        l=log_status_notification()
        x=json.loads(l)
        d["LogStatusNotification"]=x
        if d["LogStatusNotification"]["Request"]["status"]=="Uploading":
            d["LogStatusNotification"]["Request"]["status"]="Uploading"
        else:
            d["LogStatusNotification"]["Request"]["status"]="Uploaded"
        return d
    except Exception as e:
        e=str(e)
        return e

def notify_monitoring():
    data=request.get_json()
    res ,req = diagnosticcp.NotifyMonitoringReport(data["request_id"],data["seq_no"],data["generated_at"])
    return json_response("NotifyMonitoringReport",res ,req)

@app.route("/diagnostic/monitoringReport", methods=["POST"])
def get_monitoring_report():
    try:
        data=request.get_json()
        res,req = diagnostic.diagnosticGetMonitoringReport(data["request_id"],data["monitoring_criteria"],data["component_variables"])
        d={}
        s=json_response("GetMonitoringReport", res, req)
        s=json.loads(s)
        d["MonitoringReport"]=s
        l=notify_monitoring()
        d["NotifyMonitoringReport"]=json.loads(l)
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/diagnostic/setMonitoringBase", methods=["POST"])
def set_monitoring_base():
    try:
        data=request.get_json()
        res,req = diagnostic.diagnosticSetMonitoringBase(data["monitoring_base"])
        d={}
        s=json_response("SetMonitoringBase", res, req)
        s=json.loads(s)
        d["SetMonitoringBase"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/diagnostic/setVariableMonitoring", methods=["POST"])
def set_variable_monitoring():
    try:
        data=request.get_json()
        res,req = diagnostic.diagnosticSetVariableMonitoring(data["monitoring_data"])
        d={}
        s=json_response("SetVariableMonitoring", res, req)
        s=json.loads(s)
        d["SetVariableMonitoring"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/diagnostic/setMonitoringLevel", methods=["POST"])
def set_monitoring_level():
    try:
        data=request.get_json()
        res,req = diagnostic.diagnosticSetMonitoringLevel(data["severity"])
        d={}
        s=json_response("SetMonitoringLevel", res, req)
        s=json.loads(s)
        d["SetMonitoringLevel"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/diagnostic/clearVariableMonitoring", methods=["POST"])
def clear_variable_monitoring():
    try:
        data=request.get_json()
        res,req = diagnostic.diagnosticClearMonitoringVariable(data["id"])
        d={}
        s=json_response("ClearVariableMonitoring", res, req)
        s=json.loads(s)
        d["ClearVariableMonitoring"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/diagnostic/customerInformation", methods=["POST"])
def customer_information():
    try:
        data=request.get_json()
        res,req = diagnostic.diagnosticCustomerInformation(data["request_id"],data['report'],data['clear'])
        d={}
        s=json_response("CustomerInformation", res, req)
        s=json.loads(s)
        d["CustomerInformation"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/diagnostic/notifyCustomerInformation", methods=["POST"])
def notify_customer_information():
    try:
        data=request.get_json()
        res,req = diagnosticcp.NotifyCustomerInformation(data['data'],data['seq_no'],data["generated_at"],data["request_id"])
        d={}
        s=json_response("NotifyCustomerInformation", res, req)
        s=json.loads(s)
        d["NotifyCustomerInformation"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

@app.route("/diagnostic/notifyEvent", methods=["POST"])
def notify_event():
    try:
        data=request.get_json()
        res,req = diagnosticcp.NotifyEvent(data["generated_at"],data['tbc'],data['seq_no'],data['event_data'])
        d={}
        s=json_response("NotifyEvent", res, req)
        s=json.loads(s)
        d["NotifyEvent"]=s
        return d
    except Exception as e:
        e=str(e)
        return e

# @app.route("/availability/heartbeat", methods=["POST"])
# def send_charger_availability_heartbeat():
    try:
        data=request.get_json()
        res, req = availabilitycp.send_charger_availability_heartbeat(data["interval"])
        d={}
        s=json_response("Heartbeat", res, req)
        s=json.loads(s)
        d["Heartbeat"]=s
        return d
    except Exception as e:
        e=str(e)+" interval should be greater than or equal to 3"
        return e

@app.route("/availability/notification", methods=["POST"])
def send_charger_availability_notification_request():   
    try:
        data=request.get_json()
        res, req = availabilitycp.send_charger_availability_notification_request(data["timestamp"],data["connector_status"],data["evse_id"],data["connector_id"])
        d={}
        s=json_response("StatusNotification", res, req)
        s=json.loads(s)
        d["StatusNotification"]=s
        return d
    except Exception as e:
        e=str(e)    
        return e

@app.route("/availability/event", methods=["POST"])
def send_charger_availability_notify_event_request():
    try:
        data=request.get_json()
        res, req = availabilitycp.send_charger_availability_notify_event_request(data["generated_at"],data["seq_no"], data["event_data"])
        d={}
        s=json_response("NotifyEvent", res, req)
        s=json.loads(s)
        d["NotifyEvent"]=s
        return d
    except Exception as e:
        e=str(e)    
        return e

@app.route("/availability/change", methods=["POST"])
def get_charger_availability_change_availability():
    try:
        data=request.get_json()
        res, req = availability.get_charger_availability_change_availability(data["operational_status"],data["evse"])
        d={}
        s=json_response("ChangeAvailability", res, req)
        s=json.loads(s)
        d["ChangeAvailability"]=s
        if data["operational_status"]=="Operative":
            l=status_notification()
            d["StatusNotification"]=json.loads(l)
        return d
    except Exception as e:
        e=str(e)    
        return e


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=2000)


