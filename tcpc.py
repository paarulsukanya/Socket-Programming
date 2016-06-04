import socket

#creating a TCP Client Socket
cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connecting to the TCP Client
cs.connect(('localhost',8000))

while 1:
	data=raw_input('Enter your Name')
	cs.send(data)
	newdata=cs.recv(1024)
	print newdata
cs.close()
