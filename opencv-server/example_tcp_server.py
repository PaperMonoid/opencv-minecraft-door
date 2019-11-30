import socket
import time

TCP_IP = "localhost"
TCP_PORT = 1069
BUFFER_SIZE = 1

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket.bind((TCP_IP, TCP_PORT))
tcp_socket.listen(1)

connection, address = tcp_socket.accept()
print("Connection address: {0}".format(address))

while True:
    connection.send("0".encode("utf-8"))
    time.sleep(1)

    print("PING")
    connection.send("1".encode("utf-8"))
    time.sleep(1)

connection.close()
