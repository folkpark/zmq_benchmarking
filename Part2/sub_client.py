import zmq

def main():
    port = 5000
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    socket.connect("tcp://34.73.68.201:%s"%port)
    print("Socket connected on port: %s"%port)
    while True:
        message = socket.recv_string()
        print(message)

if __name__ == "__main__":
    main()