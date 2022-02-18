import db_conf
import traceback

try:
	connection = db_conf.mysql_connector()
	sql = "insert into activity values(%s,%s)"
	# val = (98,'kho-kho') # this is for single entry
	val = [(98,'kho-kho'),(88,'archery'),(74,'video games'),(45,'footbal')] # this for multiple entries
	cursor = connection.cursor()
	# cursor.execute(sql,val)# this is for single entry
	cursor.executemany(sql,val) # this for multiple entries
	connection.commit()

except Exception as e:
	print(traceback.print_tb(e._traceback_))
	print(e)

finally:
	connection.close()
	cursor.close()
