import socket
import threading
import platform
import time

# client inside the IS and who sends legal system info to the second client

SECOND_CLIENT_ADDRESS = ('127.0.0.1', 65012)
FIRST_CLIENT_ADDRESS = ('127.0.0.1', 65011)
PROXY_ADDRESS = ('127.0.0.1', 65010)

print("Client 1 has started")
time_parameter = 5


soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(PROXY_ADDRESS)


def listener():
    while True:
        buffer = platform.architecture()
        while buffer:
            soc.sendto(buffer, PROXY_ADDRESS)
            buffer = platform.architecture()


if __name__ == '__main__':
    listener()