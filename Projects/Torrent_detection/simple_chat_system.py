import socket

# creating server
def server_for_msg():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = "192.168.98.1"
    port = 5469
    s.bind((ip,port))
    s.listen()
    while True:
        print("lets start")
        con,addrs = s.accept()
        data = con.recv(1024)
        print(data)
        con.send(input("enter the msg: ").encode())
        print(addrs)
        con.close()

if __name__=="__main__":
    server_for_msg()