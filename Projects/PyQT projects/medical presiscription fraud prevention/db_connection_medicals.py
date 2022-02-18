import mysql.connector

def mysql_connect():
	my_conf = {
	'host': '192.168.98.128',
	'port': 3306,
	'user': 'MEDICAL_STAFF',
	'password': 'ashwin1',
	'database': 'medical_prescription'
	}
	cnx = mysql.connector.connect(**my_conf)
	return cnx
	