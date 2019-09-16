import socket

HOST = '127.0.0.1'
PORT = 65432
BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    conn, addr = server.accept()
    with conn:
        print("Connected by ", addr)
        while True:
            data = conn.recv(BUFFER)
            if not data:
                break
            conn.send(data)
