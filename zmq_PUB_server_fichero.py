import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:55555")


while True:
        sleep(1)
        socket.send(b"Hello World")



