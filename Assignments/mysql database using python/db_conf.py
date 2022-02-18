import mysql.connector

def mysql_connector():
	mysql_conf = {
	'host': "192.168.98.128",
	'port': 3306,
	'user': 'rockstar',
	'password': 'ashwin95',
	'database': 'experiment'
	}
	connection_establishing = mysql.connector.connect(**mysql_conf)
	return connection_establishing