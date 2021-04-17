from scapy.all import *
import socket

# client outside the IS who recieves the legal info as well as secrete message that was added by proxy

SECOND_CLIENT_ADDRESS = ('127.0.0.1', 65012)
FIRST_CLIENT_ADDRESS = ('127.0.0.1', 65011)
PROXY_ADDRESS = ('127.0.0.1', 65010)


print("Client 2 has started")


soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp - "socket.SOCK_DGRAM", tcp - Stream
soc.bind(SECOND_CLIENT_ADDRESS)
soc.connect(PROXY_ADDRESS)


def listener():
    while True:
        data = soc.recv(1024).decode()
        pac = sniff(filter="src port 65012 and dst port 65011")
        decoder(pac)
        msg = data.decode('utf-8')
        print(msg)


def decoder(pac):
    covert_message = ''
    if pac.ttl == 20:
        covert_message.append(1)
    elif pac.ttl == 220:
        covert_message.append(0)
    else:
        print(covert_message)



if __name__ == '__main__':
    listener()