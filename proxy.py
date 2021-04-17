import socket
import threading
import time
import platform
import base64
import scapy
import random
import os
from scapy.all import *
from scapy.layers.inet import *

SECOND_CLIENT_ADDRESS = ('127.0.0.1', 65012)
FIRST_CLIENT_ADDRESS = ('127.0.0.1', 65011)
PROXY_ADDRESS = ('127.0.0.1', 65010)

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(PROXY_ADDRESS)

# Имитация сетевого экрана


def listener():
    while True:
        data, address = soc.recvfrom(1024)
        if address[1] == 65011:
            soc.sendto(data, SECOND_CLIENT_ADDRESS)
        if address[1] == 65012:
            soc.sendto(data, FIRST_CLIENT_ADDRESS)


def sniffer():
    sniff(prn=agent_ttl())


def agent_ttl(covert_message, payload):
    lst = list(covert_message)
    for ind in range(len(lst)):
        if lst[ind] == "1":
            ip_header = IP(src=packet['IPv4'].src, dst='::1', ttl=20)
            udp_header = UDP(sport=packet['UDP'].sport, dport=65012)
            packet_cov = ip_header / udp_header / payload.encode('utf-8')
            send(packet_cov)
        if lst[ind] == '0':
            ip_header = IP(src=packet['IPv4'].src, dst='::1', ttl=200)
            udp_header = UDP(sport=packet['UDP'].sport, dport=65012)
            packet_cov = ip_header / udp_header / payload.encode('utf-8')
            send(packet_cov)


def agent_qos(covert_message):
    lst = list(covert_message)
    for i in range(1, len(lst), 8):
        ip_header = IP(src=packet['IPv4'].src, dst='::1', tos=covert_message[i, i + 8])
        udp_header = UDP(sport=packet['UDP'].sport, dport=65012)
        packet_cov = ip_header / udp_header / ''.encode('utf-8')
        send(packet_cov)



soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(PROXY_ADDRESS)


# here we input a covert message

print('Enter the covert message')
msg = ''
while True:
    secret_message = input()
    list_of_symbols = list(secret_message)
    continue

if __name__ == '__main__':
    listener()



    # if len(list_of_symbols) != 5:
    #     print('Введено неправильное количество символов')
    #     continue
    # error_counter = 0
    # for i in range(len(list_of_symbols)):
    #     if list_of_symbols[i] != '0' and list_of_symbols[i] != '1':
    #         error_counter += 1
    #         break
    # if error_counter == 0:
    #     print('Введённая последовательность принята, начинаю передачу...')
    #     msg = secret_message
    #     break
    # else:
    #     print('Введённая строка состоит не только из "0" и "1"')
    #     continue



