import selectors
import socket

HOST = '127.0.0.1'
PORT = 65432
BUFFER = 1024

selector = selectors.DefaultSelector()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print('listen on', (HOST, PORT))
server.setblocking(False)
selector.register(server, selectors.EVENT_READ, data=None)

while True:
    events = selector.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)

