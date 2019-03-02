import sys
import zmq

port = "5556"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect("tcp://34.73.68.201:%s" % port)

# Subscribe to zipcode, default is NYC, 10001
topicfilter = "10001"
socket.setsockopt(zmq.SUBSCRIBE)

# Process 5 updates
total_value = 0
for update_nbr in range (5):
    string = socket.recv()
    print(string)