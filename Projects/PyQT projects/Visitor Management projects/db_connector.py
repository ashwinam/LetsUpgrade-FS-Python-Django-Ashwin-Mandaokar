import mysql.connector

def mysql_connect():
    myConf = {
        'host' : '192.168.98.128',
        'port' : 3306,
        'user' : 'inviter',
        'password' : '12345678',
        'database' : 'visitor_mgmt'
    }
    cnx = mysql.connector.connect(**myConf)
    return cnx