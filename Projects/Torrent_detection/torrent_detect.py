import os
import socket
import time

def get_data():
	resp = os.popen("tasklist")
	data = resp.read()
	if 'torrent' in data:
		return True
	else:
		return False
	# raw_list = []
	# for i in resp:
	# 	raw_list.append(i.strip())
	# raw_list = raw_list[3:]

	# final_list = []
	# for final in raw_list:
	# 	final = final.rsplit(" ",40)
	# 	final_list.append(final[0].strip())

	# return (final_list)


def checking_credential():
	list_of_tasklists = get_data()
	for task in list_of_tasklists:
		if 'torrent' in task.lower():
			# "call a sending alert function"
			# create a udp server that sending the alert
			# print(task)
			sending_alert()
		else:
			continue
	print("running...")


def sending_alert():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	host = "192.168.98.128"
	port = 6666
	while True:
		if get_data():
			print("sending alerts")
			s.sendto("This computer uses the Torrent".encode(),((host,port)))
			time.sleep(10)
		# s.close()
	

if __name__=="__main__":
	# checking_credential()
	sending_alert()
	# print(get_data())



def tcp_host():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	host = "192.168.98.1"
	port = 6666
	s.bind((host,port))
	s.listen()
	while True:
		print("Server is running")
		conn,address = s.accept()
		data = conn.recv(1024)
		print(data)
		conn.send(input("please enter: ").encode())
		print("connected", address)
		conn.close()
	

# tcp_host()

def udp_host():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	host = "192.168.98.1"
	port = 6666
	s.bind((host,port))
	
	print("Server is running")
	data, addr = s.recvfrom(1024)
	print(data)
	print (addr, "Now Connected")


	
# udp_host()

