import socket

HOST = '127.0.0.1'
PORT = 65432
BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    while True:
        message = input('write a message: ')
        if not message:
            break
        client.sendall(message.encode())
        data = client.recv(BUFFER)
        print('Recived: %s' % repr(data))
