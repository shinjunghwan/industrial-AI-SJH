import socket
import sys

HOST = '127.0.0.1'
PORT = 10000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

client_socket.sendall('test'.encode())

data = client_socket.recv(1024)
print('Received', repr(data.decode()))

client_socket.close()