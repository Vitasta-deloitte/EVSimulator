#pip install psycopg2-binary
import psycopg2
import psycopg2.extras
db_instance_name = "huex-new"
db_name = "simulator"
db_password = "*H&rC*(gjpT<pQ)z"
db_port = "5432"
db_private_ip = "10.109.178.43"
db_username = "simulator-user"
# need to get postgres acces
# implement a seprate layer
# frontend <= /rest api service -> simulator () get repsonse 
#CSMS spring -> postgres dataobject
#transaction implement 
# we can something java webs sokect block this  reserveNow
#pythion
#after goe to postgres 
# that hava spring postgres "Reservenow"
try:
    with psycopg2.connect(
                host = db_private_ip,
                dbname = db_name,
                user = db_username,
                password = db_password,
                ) as conn:
        print(conn)
        # with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        #     cur.execute('DROP TABLE IF EXISTS request')
        #     cur.execute('DROP TABLE IF EXISTS response')
        #     cur.execute('DROP TABLE IF EXISTS action')
        #     # Request 
        #     create_script = ''' CREATE TABLE request (
        #                     id serial NOT NULL PRIMARY KEY,
        #                     job_id varchar,
        #                     info json NOT NULL
        #                     );'''
        #     cur.execute(create_script)
        #     insert_script = ''' INSERT INTO request (job_id,info) VALUES (%s ,%s)'''
        #     insert_values = [
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e6','{"id":0,"expiryDateTime":"12/8/2022","idToken":{"idToken":"001681020002","type":"Central"},"connectorType":"cCCS1"}'), 
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e7','{"id":0,"expiryDateTime":"12/8/2022","idToken":{"idToken":"001681020001","type":"Central"},"connectorType":"cCCS1"}'),
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e8','{"id":0,"expiryDateTime":"12/8/2022","idToken":{"idToken":"001681020001","type":"Central"},"connectorType":"cCCS1"}'),
        #     ]
        #     for record in insert_values:
        #         cur.execute(insert_script, record)
        #     cur.execute('SELECT * FROM request')
        #     for record in cur.fetchall():
        #         print(record['job_id'], " -> " ,record['info'])
        #     # Response
        #     create_script = ''' CREATE TABLE response (
        #                     id serial NOT NULL PRIMARY KEY,
        #                     job_id varchar,
        #                     info json NOT NULL
        #                     );'''
        #     cur.execute(create_script)
        #     insert_script = ''' INSERT INTO response (job_id,info) VALUES (%s ,%s)'''
        #     insert_values = [
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e6','{"status":"Accepted"}'), 
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e7','{"status":"Rejected"}'),
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e8','{"status":"Accepted"}'),
        #     ]
        #     for record in insert_values:
        #         cur.execute(insert_script, record)
        #     cur.execute('SELECT * FROM response')
        #     for record in cur.fetchall():
        #         print(record['job_id'], " -> " ,record['info'])
        #     # action
        #     create_script = ''' CREATE TABLE action (
        #                     id serial NOT NULL PRIMARY KEY,
        #                     job_id varchar,
        #                     action_key varchar,
        #                     UNIQUE (action_key)
        #                     );'''
        #     cur.execute(create_script)
        #     insert_script = ''' INSERT INTO action(job_id,action_key) VALUES (%s ,%s)'''
        #     insert_values = [ 
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e9','ReserveNow'),
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e7','TransactionEvent'),
        #     ]
        #     for record in insert_values:
        #         cur.execute(insert_script, record)
        #     cur.execute('SELECT * FROM action')
        #     for record in cur.fetchall():
        #         print(record['job_id'], " -> " ,record['action_key'])
        #     update_script = 'UPDATE action SET job_id = %s WHERE action_key = %s'
        #     update_value = [
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e9','ReserveNow'), 
        #         ('d1909b28-1959-49af-999a-bd5fdfd778e7','TransactionEvent'),
        #     ]
        #     for record in update_value:
        #         cur.execute(update_script, record)
        #     cur.execute('SELECT * FROM action')
        #     for record in cur.fetchall():
        #         print(record['job_id'], " -> " ,record['action_key'])
except Exception as error:
    print(error)
finally:
    if conn:
        conn.close()