import db_conf
import traceback

def insert(data,table):
	try:
		connection = db_conf.mysql_connector()
		sql = "insert into activity values(%s,%s)"
		cursor = connection.cursor()
		cursor.execute(sql,data) # this for multiple entries
		connection.commit()

	except Exception as e:
		print(traceback.print_tb(e._traceback_))
		print(e)

	finally:
		connection.close()
		cursor.close()

def bulk_insertion(data,table):
	try:
		connection = db_conf.mysql_connector()
		sql = "insert into activity values(%s,%s)"
		cursor = connection.cursor()
		cursor.executemany(sql,data) # this for multiple entries
		connection.commit()

	except Exception as e:
		print(traceback.print_tb(e._traceback_))
		print(e)

	finally:
		connection.close()
		cursor.close()

def download(table):
	try:
		connection = db_conf.mysql_connector()
		sql = f"select * from {table}"
		cursor = connection.cursor()
		cursor.execute(sql)
		rows = cursor.fetchall()
		return (rows)

	except Exception as e:
		print(traceback.print_tb(e._traceback_))
		print(e)

	finally:
		connection.close()
		cursor.close()

