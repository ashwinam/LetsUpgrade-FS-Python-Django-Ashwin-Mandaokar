import db_conf
import traceback

try:
	connection = db_conf.mysql_connector()
	sql = "select * from activity"
	cursor = connection.cursor()
	cursor.execute(sql)
	rows = cursor.fetchall()
	print(rows)

except Exception as e:
	print(traceback.print_tb(e._traceback_))
	print(e)

finally:
	connection.close()
	cursor.close()
