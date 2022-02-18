import db_connection_doctor, db_connection_medicals, traceback

def insert(table,data):
	try:
		cnx = db_connection_doctor.mysql_connect()
		sql = f"INSERT INTO {table}(doctor_id,patient_id,medicines,otp) values(%s,%s,%s,%s)"
		cursor = cnx.cursor()
		cursor.execute(sql,data)
		cnx.commit()

	except Exception as e:
		print(e)
		print(traceback.print_tb(e.__traceback__))

	finally:
		cnx.close()
		cursor.close()

def Retrieve_row(table,id_no):
	try:
		cnx = db_connection_medicals.mysql_connect()
		cursor = cnx.cursor()
		sql = f"select doctor_id,patient_id,medicines,otp from {table} where id = %s"
		cursor.execute(sql,(id_no, ))
		rows = cursor.fetchall()
		for doctor_id,patient_id,medicines,otp in rows:
			return str(doctor_id),str(patient_id),medicines,otp

	except Exception as e :
		print (traceback.print_tb(e.__traceback__))
		print (e)
	
	finally:
		cnx.close()
		cursor.close()

def update(table,status,id_no):
		try:
			cnx = db_connection_medicals.mysql_connect()
			cursor = cnx.cursor()
			sql = f"update {table} set status = '{status}' where id = %s"
			cursor.execute(sql, (id_no, ))
			cnx.commit()


		except Exception as e:
			print (traceback.print_tb(e.__traceback__))
			print (e)
		
		finally:
			cnx.close()
			cursor.close()