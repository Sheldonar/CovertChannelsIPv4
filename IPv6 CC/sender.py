import socket
import platform
from time import sleep

RECEIVER_ADDR = ('::1', 10001)
SENDER_ADDR = ('::1', 10002)
PROXY_ADDR = ('::1', 10003)
SECOND_RECEIVER_ADDR = ('::1', 10004)


def sender():
    try:
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.bind(SENDER_ADDR)

        with True:
            message = platform.processor()
            sock.sendto(bytes(message, 'utf-8'), RECEIVER_ADDR)
            sleep(3)

    except Exception as ex:
        print(ex)
    finally:
        sock.close()


if __name__ == '__main__':
    sender()