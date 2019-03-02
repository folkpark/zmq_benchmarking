import zmq
import time

context = zmq.Context()
socket0 = context.socket(zmq.PUB)
socket0.bind("tcp://*:5000")
print("Waiting 7 seconds to allow client(s) to connect")

# Sleep a bit of time until the connection is properly established,
# otherwise some messages may be lost.
# http://stackoverflow.com/questions/7470472/lost-messages-on-zeromq-pub-sub
time.sleep(7)
for i in range(100):
    message = "foo {}".format(i)
    print("Sending a '%s' as a message"%message )
    socket0.send_string(message)
    time.sleep(1)