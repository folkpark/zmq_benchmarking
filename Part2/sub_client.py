import zmq
import sys

def main():
    port = 5000
    if len(sys.argv) == 0:
        port = sys.argv[0]
        print("Setting port number to %s"%port)

    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    # accept all topics (prefixed) - default is none
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    socket.connect("tcp://34.73.68.201:%s"%port)
    print("Socket connected on port: %s"%port)
    while True:
        message = socket.recv_string()
        print(message)

if __name__ == "__main__":
    main()