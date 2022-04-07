import socket
import sys
import RPi.GPIO as GPIO

PORT = 10000
pin = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)
pwm.start(1)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', PORT))
server_socket.listen(10)

client_socket, addr = server_socket.accept()

print('Connected by', addr)

while True:
    data = 0
    while not data:
        data = client_socket.recv(1024)
    
    pwm.start(int(data.decode()))
    print('Received from', addr, data.decode())
    client_socket.sendall(data)
    
client_socket.close()
server_socket.close()
