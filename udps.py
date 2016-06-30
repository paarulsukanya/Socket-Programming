import socket

port = 8000
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost", port))

print "waiting on port:", port

while True:
    data, address = server.recvfrom(1024)
    print "Hello, %s" % data