import zmq
import time

context = zmq.Context()
socket0 = context.socket(zmq.PUB)
socket1 = context.socket(zmq.PUB)
socket2 = context.socket(zmq.PUB)
socket3 = context.socket(zmq.PUB)
socket4 = context.socket(zmq.PUB)
#Bind on the different ports. UOncomment as needed to add more nodes.
#Note that if a client doesn't connect to the socket in time the program
#may not run.
socket0.bind("tcp://*:5000")
socket1.bind("tcp://*:5001")
socket2.bind("tcp://*:5002")
socket3.bind("tcp://*:5003")
socket4.bind("tcp://*:5004")
print("Waiting 7 seconds to allow client(s) to connect")

# Sleep a bit of time until the connection is properly established,
# otherwise some messages may be lost.
# http://stackoverflow.com/questions/7470472/lost-messages-on-zeromq-pub-sub
time.sleep(7)

for i in range(100):
    message = "foo {}".format(i)
    print("Sending a '%s' as a message"%message )
    socket0.send_string(message)
    socket1.send_string(message)
    socket2.send_string(message)
    socket3.send_string(message)
    socket4.send_string(message)
    time.sleep(1)