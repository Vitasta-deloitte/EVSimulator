id= 1
expiry_date_time= "12/8/2022"
id_token={ "idToken": "001681020001", "type": "Central" }
connector_type= "cCCS1"
evse_id= 0
group_id_token= {"idToken":"22","type":"Central"}
var=[]
# var.append(f'cp.send_reservation({id},"{expiry_date_time}",{id_token},"{connector_type}",{evse_id},{group_id_token})')

reservation_id=0
var.append(f'cp.send_cancel_reservation({reservation_id})')