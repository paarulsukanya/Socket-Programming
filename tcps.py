import socket

#creating TCP Server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding Server socket to local host
s.bind(('localhost',8000))

#Server socket listens for any client request
s.listen(1)

#Server Socket accepts client request on socket 'cs'
cs,addr=s.accept()
print 'Connection from ', addr

while 1:
	data=cs.recv(1024)
	newdata="Hi,"+data
	cs.send(newdata)
cs.close()
