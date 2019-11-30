import socket
import datetime


TCP_IP = "localhost"
TCP_PORT = 1069
BUFFER_SIZE = 1

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((TCP_IP, TCP_PORT))

while True:
    data = tcp_socket.recv(BUFFER_SIZE)
    if data == "1":
        print(datetime.datetime.now())

s.close()
