import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
host = 'localhost';
port = 8000;
 
while True:
    msg = raw_input('whats your name?')
    client.sendto(msg, (host, port))
         
