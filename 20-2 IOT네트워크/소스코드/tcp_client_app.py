import socket
import sys
import time
from struct import pack

HOST = '192.168.0.4'
PORT = 10000
a = '1'
b = 1
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
 
while True:
    
    client_socket.sendall(str(b).encode())
    data = 0
    while not data:
        data = client_socket.recv(1024)
    print('Received', repr(data.decode()))
    time.sleep(0.1)
    if b > 99:
        b = 1
    else:
        b = b+1

client_socket.close()