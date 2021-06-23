import socket
import sys
import select

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

while True:
    sockets_list = [sys.stdin, client]

    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == client:
            message = socks.recv(2048)
            print(message.decode())
        else:
            message = sys.stdin.readline()
            client.send(message.encode('utf-8'))
            sys.stdout.flush()
