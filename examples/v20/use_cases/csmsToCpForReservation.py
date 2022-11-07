from datetime import datetime as dt


id= 1
expiry_date_time= "12/10/22"
id_token={ "idToken": "001681020001", "type": "Central" }
connector_type= "cCCS1"
evse_id= 1
group_id_token= {"idToken":"22","type":"Central"}
var=[]

#S1 - Reserve a unspecified EVSE at a Charging Station
id=1
evse_id=0

#S2 - Reserve a specified EVSE at a Charging Station
# connector_type="Unknown"

# #S3 - Reserve a connector type at a Charging Station
# connector_type="Unknown"
# evse_id=0

##Comparing date
# date="12/09/22"
# a = dt.strptime(expiry_date_time, "%d/%m/%y")
# b = dt.strptime(date, "%d/%m/%y")

# if b<=a:
#     expiry_date_time=expiry_date_time
# else:
#     id=0

var.append(f'cp.send_reservation({id},"{expiry_date_time}",{id_token},"{connector_type}",{evse_id},{group_id_token})')

# reservation_id=1
# var.append(f'cp.send_cancel_reservation({reservation_id})')