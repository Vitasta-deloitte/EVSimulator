
var=[]
timestamp="1666775586"
connector_status="Available"
evse_id=1
connector_id=1
var.append(f'cp.send_status_notification("{timestamp}","{connector_status}",{evse_id},{connector_id})')