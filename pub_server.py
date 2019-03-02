import zmq
import random
import sys
import time

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
    topic = random.randrange(9999,10005)
    messagedata = (b"Hello World on Topic: %s")
    socket.send(messagedata)
    time.sleep(1)